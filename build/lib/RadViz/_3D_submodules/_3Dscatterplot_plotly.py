# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 23:37:52 2020

@author: elewah
"""

# =============================================================================
# #plotRadviz3D function is created to draw the prepared dataframe using plotty 3D scatter plot 
# #input is the prepared dataframe and the output is the 3D RadViz plot
# =============================================================================
import plotly.express as px
def plotRadviz3D(df):
    ##chose the colors for the labels 
    color_sequence=["white"]
    for i in px.colors.qualitative.Plotly[1:]:
        color_sequence.append(i)
    color_sequence.append(px.colors.qualitative.Plotly[0])
    for i in px.colors.qualitative.Set2:
        color_sequence.append(i)
    for i in px.colors.qualitative.Pastel:
        color_sequence.append(i)
#     google_color=['#F44236','#E91D62','#363F46','#9C26B0','#3E50B4','#02A8F4','#019587','#8BC24A','#FFE93B','#FF9700','#7F5549','#9D9D9D', '#607C8A']
#     for i in google_color:
#         color_sequence.append(i)
    df.rename(columns={'index': 'label'},inplace=True)
    fig = px.scatter_3d(df, x='x', y='y', z='z',
              color='label',text='AnchorsLabel', color_discrete_sequence=color_sequence,opacity=0.999999999999)
    fig.show() 