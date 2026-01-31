# File: radviz_plotly/_3D_submodules/sorting_utils.py
# -*- coding: utf-8 -*-
"""
Created for 3D RadViz with Attribute Sorting

This module contains utilities for sorting and grouping attributes based on correlations
to optimize RadViz anchor placement.
"""

import numpy as np
import pandas as pd
from numpy import pi, cos, sin, arccos, arange

try:
    from sklearn.cluster import KMeans
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False
    print("Warning: sklearn not available. RadViz3D_withSorting will not work without it.")

try:
    import transformations as trafo
    TRANSFORMATIONS_AVAILABLE = True
except ImportError:
    TRANSFORMATIONS_AVAILABLE = False
    print("Warning: transformations not available. RadViz3D_withSorting will not work without it.")

from radviz_plotly._3D_submodules.points_onsphere import get_3Dpoints


def unique(list1):
    """
    Get unique values from a list while preserving order.
    
    Parameters
    ----------
    list1 : list
        Input list
        
    Returns
    -------
    list
        List with unique values
    """
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


def Anchorsgrouping(data, fineTuningFactor):
    """
    Group attributes based on correlation pairs above a threshold.
    
    Parameters
    ----------
    data : DataFrame
        Features dataframe
    fineTuningFactor : float
        Correlation threshold for grouping
        
    Returns
    -------
    tuple
        (groups, numberOfAttributes) - List of attribute groups and total count
    """
    d = data.columns.size
    matrix = np.triu(data.corr())
    ArrangedCorrPairs = data.corr().unstack().sort_values(ascending=False).to_frame()
    
    cutSelfCorr = ArrangedCorrPairs[d:]  # Remove self-correlations
    cutSelfCorr.reset_index(inplace=True)
    
    cutRepetition = cutSelfCorr[cutSelfCorr.index % 2 != 0]
    
    positvecorr = cutRepetition[cutRepetition[0] > fineTuningFactor]
    positvecorr.reset_index(inplace=True, drop=True)
    
    pairsList = []
    for i in positvecorr.index:
        pairsList.append([positvecorr.iloc[i, 0], positvecorr.iloc[i, 1]])
    
    groupslist = list(list())
    savingindex = []
    groupNumber = 0
    
    while len(pairsList) != 0:
        groupslist.append(pairsList[0])
        for i in range(len(pairsList)):
            if groupslist[groupNumber][0] in pairsList[i]:
                groupslist[groupNumber].append(pairsList[i][0])
                groupslist[groupNumber].append(pairsList[i][1])
            elif groupslist[groupNumber][1] in pairsList[i]:
                groupslist[groupNumber].append(pairsList[i][0])
                groupslist[groupNumber].append(pairsList[i][1])
            else:
                savingindex.append(i)
        pairsList = [pairsList[index] for index in savingindex]
        
        # Second wave
        savingindex = []
        for i in range(len(pairsList)):
            if pairsList[i][0] not in groupslist[groupNumber]:
                if pairsList[i][1] not in groupslist[groupNumber]:
                    savingindex.append(i)
        pairsList = [pairsList[index] for index in savingindex]
        
        groupNumber = groupNumber + 1
        savingindex = []
    
    groups = list(list())
    for i in range(len(groupslist)):
        groups.append(unique(groupslist[i]))
    
    numberOfAtributes = 0
    for i in groups:
        numberOfAtributes = numberOfAtributes + len(i)
    
    return groups, numberOfAtributes


def deepCorrelatorsGroups(data):
    """
    Analyze correlations to create optimal attribute groups.
    Groups highly correlated attributes together and separates negatively correlated ones.
    
    Parameters
    ----------
    data : DataFrame
        Features dataframe
        
    Returns
    -------
    tuple
        (worstEnemiesGroups, numberOfAttributes) - Optimally arranged groups and total count
    """
    d = data.columns.size
    
    # Find best tuning factor
    BestTunedFactor = 0
    for i in range(100):
        fineTuningFactor = i / 100.0
        groups, numberOfAtributes = Anchorsgrouping(data, fineTuningFactor)
        if numberOfAtributes == d:
            BestTunedFactor = fineTuningFactor
    
    groups, numberOfAtributes = Anchorsgrouping(data, BestTunedFactor)
    
    # Find worst enemies (negatively correlated attributes)
    matrix = np.triu(data.corr())
    ArrangedCorrPairs = data.corr().unstack().sort_values(ascending=True).to_frame()
    
    cutSelfCorr = ArrangedCorrPairs
    cutSelfCorr.reset_index(inplace=True)
    
    cutRepetition = cutSelfCorr[cutSelfCorr.index % 2 != 0]
    
    worestEnemies = cutRepetition[cutRepetition[0] < 0]
    worestEnemies.reset_index(inplace=True, drop=True)
    
    pairsList = []
    for i in worestEnemies.index:
        pairsList.append([worestEnemies.iloc[i, 0], worestEnemies.iloc[i, 1]])
    
    groupIndex = []
    for pairs in pairsList:
        for i in range(len(groups)):
            if pairs[0] in groups[i]:
                if i not in groupIndex:
                    groupIndex.append(i)
            if pairs[1] in groups[i]:
                if i not in groupIndex:
                    groupIndex.append(i)
    
    worestEnemiesGroups = []
    for i in groupIndex:
        worestEnemiesGroups.append(groups[i])
    
    numberOfAtributes = 0
    counter = 0
    groupNumber = 1
    for i in worestEnemiesGroups:
        counter = counter + 1
        numberOfAtributes = numberOfAtributes + len(i)
        print(f"Number of attributes in group {groupNumber} is {len(i)}")
        groupNumber = groupNumber + 1
    
    print("The groups after applying worst enemies arrangement:")
    print(worestEnemiesGroups)
    
    return worestEnemiesGroups, numberOfAtributes


def worstEnemiesAnchorsSorting(anchorsCenterMax, numberOfGroups):
    """
    Sort anchor centers to maximize distance between them (worst enemies placement).
    
    Parameters
    ----------
    anchorsCenterMax : DataFrame
        DataFrame with x, y, z coordinates of anchor centers
    numberOfGroups : int
        Number of groups
        
    Returns
    -------
    DataFrame
        Sorted anchor centers with maximum distance between consecutive points
    """
    anchorsCenterMax_worstEnemies = pd.DataFrame(columns=['x', 'y', 'z'])
    anchorsCenterMax_worstEnemies = pd.concat(
        [anchorsCenterMax_worstEnemies, anchorsCenterMax[0:1]], sort=False
    )
    
    for i in range(numberOfGroups - 1):
        diff = anchorsCenterMax - anchorsCenterMax.iloc[0]
        diffpw2 = diff ** 2
        anchorsCenterMax['AnchorsDistance'] = diffpw2.sum(axis=1, skipna=True)
        anchorsCenterMax['AnchorsDistance'] = anchorsCenterMax['AnchorsDistance'] ** (1 / 2)
        anchorsCenterMax.sort_values(by='AnchorsDistance', inplace=True, ascending=False)
        anchorsCenterMax_worstEnemies = pd.concat([
            anchorsCenterMax_worstEnemies,
            anchorsCenterMax[0:1].drop(['AnchorsDistance'], axis=1)
        ])
        anchorsCenterMax.drop(anchorsCenterMax.tail(1).index, inplace=True)
    
    return anchorsCenterMax_worstEnemies


def get_AnchorsWithKmeans(num_pts, numberOfClusters):
    """
    Generate anchors using K-means clustering on sphere points.
    
    Parameters
    ----------
    num_pts : int
        Number of points to generate on sphere
    numberOfClusters : int
        Number of clusters for K-means
        
    Returns
    -------
    tuple
        (KmeansClusterCenters, anchorsnormal, HDunitspherepoints)
    """
    if not SKLEARN_AVAILABLE:
        raise ImportError("sklearn is required for this function. Install it with: pip install scikit-learn")
    if not TRANSFORMATIONS_AVAILABLE:
        raise ImportError("transformations is required for this function. Install it with: pip install transformations")
    
    HDunitspherepoints = get_3Dpoints(num_pts)
    X = HDunitspherepoints.to_numpy()
    
    kmeans = KMeans(n_clusters=numberOfClusters, random_state=42)
    kmeans.fit(X)
    y_kmeans = kmeans.predict(X)
    
    label = y_kmeans.astype(str)
    HDunitspherepoints = pd.DataFrame({
        'label': label,
        'x': HDunitspherepoints['x'],
        'y': HDunitspherepoints['y'],
        'z': HDunitspherepoints['z']
    })
    
    normal = trafo.unit_vector(kmeans.cluster_centers_, axis=1)
    anchorsnormal = pd.DataFrame({
        'label': 'normalize-lenses-focus',
        'x': normal[:, 0],
        'y': normal[:, 1],
        'z': normal[:, 2]
    })
    
    KmeansClusterCenters = pd.DataFrame({
        'label': 'lenses focus',
        'x': kmeans.cluster_centers_[:, 0],
        'y': kmeans.cluster_centers_[:, 1],
        'z': kmeans.cluster_centers_[:, 2]
    })
    
    return KmeansClusterCenters, anchorsnormal, HDunitspherepoints


def GetSortedAnchors(nInEachGroup):
    """
    Generate sorted anchors for each attribute group.
    
    Parameters
    ----------
    nInEachGroup : array
        Array with number of attributes in each group
        
    Returns
    -------
    DataFrame
        Sorted anchors DataFrame with x, y, z coordinates
    """
    df = pd.DataFrame(columns=['x', 'y', 'z', 'AnchorsDistance'])
    numberOfAnchors = nInEachGroup.sum()
    numberOfGroups = len(nInEachGroup)
    
    num_pts_1 = numberOfGroups * 10000
    KmeansClusterCenters, anchorsCenterMax, HDunitspherepoints = get_AnchorsWithKmeans(
        num_pts_1, numberOfGroups
    )
    
    anchorsCenterMax.drop(['label'], axis=1, inplace=True)
    
    anchorsMax = get_3Dpoints(numberOfAnchors * 10)
    
    anchorsCenterMax = worstEnemiesAnchorsSorting(anchorsCenterMax, numberOfGroups)
    
    for i in range(numberOfGroups):
        diff = anchorsMax - anchorsCenterMax.iloc[i]
        diffpw2 = diff ** 2
        anchorsMax['AnchorsDistance'] = diffpw2.sum(axis=1, skipna=True)
        anchorsMax['AnchorsDistance'] = anchorsMax['AnchorsDistance'] ** (1 / 2)
        anchorsMax.sort_values(by='AnchorsDistance', inplace=True)
        
        df = pd.concat([df, anchorsMax[0:nInEachGroup[i]]])
        anchorsMax = anchorsMax[nInEachGroup[i]:]
    
    label = np.full(int(nInEachGroup[0]), str(0))
    for i in range(numberOfGroups - 1):
        label = np.concatenate(
            (label, np.full(int(nInEachGroup[i + 1]), str(i + 1))),
            axis=None
        )
    
    df['label'] = label
    df.reset_index(inplace=True, drop=True)
    df = df.drop(['AnchorsDistance'], axis=1)
    
    anchorsCenterMax['label'] = 'X'
    frames = [df, anchorsCenterMax]
    df1 = pd.concat(frames)
    
    return df