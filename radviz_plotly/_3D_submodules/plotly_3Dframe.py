# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 23:30:48 2020

@author: elewah
"""

# =============================================================================
# #Dataframe3DPreparation function is created to Concatenate 3 matrixs,
# #S_hat matrix"mapped version of records "& X matrix"Dimensions Anchors" &Circle matrix "Circle Boundery matrix" 
# #input are S_hat matrix(samples or Records matrix) and X matrix (dimensions' anchors matrix),
# #and BPs stand for Number of boundery points that will be used to draw the bounderies of the RadViz space 
# #Output are the prepared dataframe that will be visualized 
# =============================================================================
import pandas as pd
import numpy as np
from radviz_plotly._3D_submodules.points_onsphere import get_3Dpoints
def Dataframe3DPreparation(S_hat,X,d,BPs,y):
    frames = [y,S_hat]
    S_hat = pd.concat(frames,axis=1)
    #print(S_hat)
    X=X.reset_index()
    ############################## show Xi Dimiensions Anchors
    AnchorsLabel=np.append( X['index'], np.full(S_hat.shape[0],'') )
    #print('AnchorsLabel')
    #print( AnchorsLabel)
    ############################## show Xi Dimiensions Anchors
    #print(X)
    label =np.full((d), 'Anchors\' Names')
    X['index']=label
    #print(X)
    ############################# show diminion boundry
    C=get_3Dpoints(BPs) 
    C= pd.DataFrame(C)
    label =np.full((BPs), 'sphere') 
    label=pd.DataFrame(label)
    label = label.rename(columns={0: 'index'})
    frames = [label,C]
    sphere = pd.concat(frames,axis=1)
    #print(sphere)
    frames = [X,S_hat]
    df = pd.concat(frames)
    df['AnchorsLabel']=AnchorsLabel
    #print(df)
    return df,sphere