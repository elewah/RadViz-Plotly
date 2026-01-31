# File: tests/test_RadViz3DSort.py
# -*- coding: utf-8 -*-
"""
Test script for RadViz3D with Sorting functionality
"""

import pandas as pd
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from radviz_plotly import RadViz3D_withSorting

def test_3d_radviz_with_sorting():
    """
    Test RadViz3D_withSorting with 3-segma dataset
    """
    print("Loading dataset...")
    data = pd.read_csv('tests/DataFolder/3-segma.csv')
    
    print(f"Dataset shape: {data.shape}")
    print(f"Columns: {list(data.columns)[:10]}...")  # Show first 10 columns
    
    # Prepare data
    y = data['index']
    X = data.drop(['index'], axis=1)
    
    print(f"\nFeatures shape: {X.shape}")
    print(f"Labels unique values: {y.unique()}")
    
    # Run RadViz3D with sorting
    print("\n" + "="*60)
    print("Running RadViz3D with Sorting...")
    print("="*60 + "\n")
    
    BPs = 10000  # Number of boundary points
    RadViz3D_withSorting(y, X, BPs)
    
    print("\nVisualization complete!")

if __name__ == "__main__":
    test_3d_radviz_with_sorting()