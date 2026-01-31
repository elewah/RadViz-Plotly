# -*- coding: utf-8 -*-
"""
3D RadViz with Attribute Sorting

This module provides 3D RadViz visualization with intelligent attribute sorting
based on correlation analysis.
"""

import pandas as pd
import numpy as np
from radviz_plotly._3D_submodules.normalizing import matrixNormlization
from radviz_plotly._3D_submodules.RadViz_mapping import Radviz3DMapping
from radviz_plotly._3D_submodules.plotly_3Dframe import Dataframe3DPreparation
from radviz_plotly._3D_submodules._3Dscatterplot_plotly import plotRadviz3D
from radviz_plotly._3D_submodules.sorting_utils import (
    deepCorrelatorsGroups,
    GetSortedAnchors
)


def RadViz3D_withSorting(y, X, BPs=10000):
    """
    3D RadViz visualization with intelligent attribute sorting.
    
    This function analyzes correlations between attributes and arranges
    dimension anchors on the sphere to minimize clutter and improve
    visualization quality. Highly correlated attributes are grouped
    together, while negatively correlated attributes are placed far apart.
    
    Parameters
    ----------
    y : pandas.Series
        Labels column for the data points
    X : pandas.DataFrame
        Features dataframe with attributes as columns
    BPs : int, optional
        Number of boundary points for sphere visualization (default: 10000)
        
    Returns
    -------
    None
        Displays the interactive 3D RadViz plot
        
    Notes
    -----
    This function requires sklearn and transformations packages:
    - pip install scikit-learn
    - pip install transformations
    
    The sorting algorithm:
    1. Analyzes correlation matrix of attributes
    2. Groups highly correlated attributes
    3. Identifies negatively correlated attribute pairs
    4. Uses K-means clustering to determine anchor positions
    5. Arranges anchors to maximize distance between negative correlations
    
    Examples
    --------
    >>> import pandas as pd
    >>> from radviz_plotly import RadViz3D_withSorting
    >>> 
    >>> data = pd.read_csv('dataset.csv')
    >>> y = data['label']
    >>> X = data.drop(['label'], axis=1)
    >>> RadViz3D_withSorting(y, X, BPs=10000)
    """
    # Rename label column
    y_copy = y.copy()
    y_copy.rename("index", inplace=True)
    
    # Normalize the data
    X = matrixNormlization(X)
    
    # Analyze correlations and group attributes
    print("Analyzing attribute correlations...")
    groups, numberOfAtributes = deepCorrelatorsGroups(X)
    
    # Prepare sorted attribute list
    sortedAttributes = []
    for i in groups:
        for e in i:
            sortedAttributes.append(e)
    
    # Count attributes per group
    nInEachGroup = []
    for i in groups:
        nInEachGroup.append(len(i))
    
    # Keep original data as S matrix
    S = X.copy()
    
    # Generate sorted anchors based on groups
    print("Generating sorted anchors...")
    X_anchors = GetSortedAnchors(np.array(nInEachGroup))
    
    # Prepare anchor matrix
    DAsLabel = X_anchors[['label']]
    X_anchors = X_anchors.drop(['label'], axis=1)
    X_anchors['DS_names'] = sortedAttributes
    X_anchors = X_anchors.set_index('DS_names')
    X_anchors.index.name = None
    
    # Reorder S matrix according to sorted attributes
    S = S[sortedAttributes]
    
    # Get column names
    DS_names = S.columns
    
    # Perform RadViz mapping
    print("Performing RadViz mapping...")
    S_hat = Radviz3DMapping(S, X_anchors)
    
    # Prepare dataframe for visualization
    d = DS_names.size
    df, df_sphere = Dataframe3DPreparation(S_hat, X_anchors, d, BPs, y_copy)
    
    # Plot the result
    print("Rendering visualization...")
    plotRadviz3D(df, df_sphere)
