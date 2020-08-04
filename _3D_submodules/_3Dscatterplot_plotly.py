# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 23:37:52 2020

@author: elewah
"""
import plotly.express as px
def plotRadviz3D(df): 
    df.rename(columns={'index': 'label'},inplace=True)
    fig = px.scatter_3d(df, x='x', y='y', z='z',
              color='label',text='AnchorsLabel')
    fig.show()