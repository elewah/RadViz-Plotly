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
import plotly.graph_objects as go 
import plotly.io as pio
def plotRadviz3D(df,df_sphere):
    pio.templates["draft"] = go.layout.Template(
        layout_annotations=
        [dict(name="draft watermark", text="",
              textangle=-30, opacity=0.1,
              font=dict(color="black", size=100), xref="paper",
              yref="paper", x=0.5, y=0.5, showarrow=False, ) ])
    #########################################
    config = {'toImageButtonOptions': {'format': 'png', # one of png, svg, jpeg, webp,svg
                                       'filename': 'custom_image',
                                        'height': 1000,
                                        'width': 1000,
                                        'scale': 1 # Multiply title/legend/axis/canvas sizes by this factor
                                      }}
    #########################################
    ##chose the colors for the labels 
    color_sequence=[]
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
    fig = go.Figure()
    fig = px.scatter_3d(df, x='x', y='y', z='z', color="label",color_discrete_sequence=color_sequence,text='AnchorsLabel')
    fig.add_trace(go.Scatter3d(mode='markers',marker=dict(size=0,color='white',opacity=0.1),
    x=df_sphere["x"],y=df_sphere["y"],z=df_sphere["z"],showlegend=False))
#     fig.update_layout(template="draft")
#     fig.show(config=config)  
    fig.show()