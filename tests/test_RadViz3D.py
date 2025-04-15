# =============================================================================
# Test script for RadViz3D function
# =============================================================================
import os
import pandas as pd
from radviz_plotly import RadViz3D
import pytest

def test_radviz3d():
    # Construct the path to the CSV file relative to the project root
    data_folder = os.path.join(os.path.dirname(__file__), 'DataFolder')
    data_file = os.path.join(data_folder, 'BreastCancer.csv')
    data = pd.read_csv(data_file)
    y = data['index']
    X = data.drop(['index'], axis=1)

    # Set number of breakpoints
    BPs = 10000

    # Call RadViz3D function
    try:
        RadViz3D(y, X, BPs)
    except Exception as e:
        pytest.fail(f"RadViz3D test failed with error: {e}")