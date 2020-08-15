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
    #label colors and it matches label colors of 3D RadViz
    color_sequence=[]
    for i in px.colors.qualitative.Plotly:
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
    fig = px.scatter(df, x=0, y=1, color='label',text='AnchorsLabel', color_discrete_sequence=color_sequence)
    fig.update_layout(
        dragmode='select',
        width=1000,
        height=1000,
        hovermode='closest')
    fig.show()