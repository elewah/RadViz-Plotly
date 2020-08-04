# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 23:30:48 2020

@author: elewah
"""
import pandas as pd
import numpy as np
from _2D_submodules.points_oncircle import get_2Dpoints
def Dataframe2DPreparation(S_hat,X,d,BPs,y):
    frames = [y,S_hat]
    S_hat = pd.concat(frames,axis=1)
    
    #print(S_hat)
    ############################## show Xi Dimiensions Anchors
    X=X.reset_index()
    ###############################################
    AnchorsLabel=np.append(np.full(BPs,''),  X['index'] )
    AnchorsLabel=np.append(AnchorsLabel, np.full(S_hat.shape[0],'') )
    ###############################################
    #print(X)
    label =np.full((d), 'X')
    X['index']=label
    #print(X)
    ############################# show diminion boundry
    C=get_2Dpoints(1, BPs) #we need to change this area to be dinamically
    C= pd.DataFrame(C)
    label =np.full((BPs), 'circle') #we need to change this area to be dinamically
    label=pd.DataFrame(label)
    label = label.rename(columns={0: 'index'})
    frames = [label,C]
    circle = pd.concat(frames,axis=1)
    #print(circle)
    frames = [circle,X,S_hat]
    df = pd.concat(frames)
    df['AnchorsLabel']=AnchorsLabel
    #print(df)
    return df