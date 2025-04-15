# =============================================================================
# Test script for RadViz2D function
# =============================================================================
import pandas as pd
from RadViz.RadViz2D import RadViz2D
import pytest

def test_radviz2d():
    # Load dataset
    data = pd.read_csv('DataFolder/BreastCancer.csv')
    y = data['index']
    X = data.drop(['index'], axis=1)

    # Set number of breakpoints
    BPs = 10000

    # Call RadViz2D function
    try:
        RadViz2D(y, X, BPs)
    except Exception as e:
        pytest.fail(f"RadViz2D test failed: {e}")