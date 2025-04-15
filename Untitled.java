# =============================================================================
# for testing purpose     
# =============================================================================

#BreastCancer
import plotly.io as pio
pio.renderers.default = "browser"   
data= pd.read_csv('DataFolder/BreastCancer.csv')
y=data['index']
X=data.drop(['index'], axis=1)
BPs=10000
RadViz3D(y,X,BPs)
RadViz2D(y,X,BPs) 