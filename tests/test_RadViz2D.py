# =============================================================================
# Test script for RadViz2D function
# =============================================================================
import os
import pandas as pd
from radviz_plotly import RadViz2D
import pytest

def test_radviz2d():
    # Construct the path to the CSV file relative to the project root
    data_folder = os.path.join(os.path.dirname(__file__), 'DataFolder')
    data_file = os.path.join(data_folder, 'BreastCancer.csv')
    data = pd.read_csv(data_file)
    y = data['index']
    X = data.drop(['index'], axis=1)

    # Set number of breakpoints
    BPs = 10000

    # Call RadViz2D function
    try:
        RadViz2D(y, X, BPs)
    except Exception as e:
        pytest.fail(f"RadViz2D test failed with error: {e}")