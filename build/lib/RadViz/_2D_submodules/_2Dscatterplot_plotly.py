# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 23:37:52 2020

@author: elewah
"""
# =============================================================================
# #plotRadviz2D function is created to draw the prepared dataframe using plotty 2D scatter plot 
# #input is the prepared dataframe and the output is the 2D RadViz plot
# =============================================================================
import plotly.express as px
def plotRadviz2D(df):
    df.rename(columns={'index': 'label'},inplace=True)
    fig = px.scatter(df, x=0, y=1, color='label',text='AnchorsLabel')
    fig.update_layout(
        title='paper data set',
        dragmode='select',
        width=1000,
        height=1000,
        hovermode='closest',)
    fig.show()