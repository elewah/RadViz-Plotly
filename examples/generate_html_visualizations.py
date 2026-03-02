"""
Generate interactive HTML visualizations for all three RadViz functions.

This script replicates the plotting logic from the package's internal modules
but returns figure objects that can be saved as HTML files.

Output: Saves HTML files to iframe_figures/ directory
"""

import pandas as pd
import numpy as np
import os
import sys
import plotly.express as px
import plotly.graph_objects as go

# Add parent directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import necessary modules for 2D RadViz
from radviz_plotly._2D_submodules.normalizing import matrixNormlization
from radviz_plotly._2D_submodules.points_oncircle import get_2Dpoints
from radviz_plotly._2D_submodules.get_anchors_matrix import get_X2Dmatrix
from radviz_plotly._2D_submodules.RadViz_mapping import Radviz2DMapping
from radviz_plotly._2D_submodules.plotly_2Dframe import Dataframe2DPreparation

# Import necessary modules for 3D RadViz
from radviz_plotly._3D_submodules.normalizing import matrixNormlization as matrixNormlization3D
from radviz_plotly._3D_submodules.points_onsphere import get_3Dpoints
from radviz_plotly._3D_submodules.get_anchors_matrix import get_X3Dmatrix
from radviz_plotly._3D_submodules.RadViz_mapping import Radviz3DMapping
from radviz_plotly._3D_submodules.plotly_3Dframe import Dataframe3DPreparation

# Import sorting utilities (optional)
try:
    from radviz_plotly._3D_submodules.sorting_utils import deepCorrelatorsGroups, GetSortedAnchors
    SORTING_AVAILABLE = True
except ImportError:
    SORTING_AVAILABLE = False
    print("Warning: Sorting dependencies not available. Skipping 3D with sorting.")


def generate_radviz2d_figure(y, X, BPs=10000):
    """
    Generate 2D RadViz figure (replicates plotRadviz2D logic).

    Parameters
    ----------
    y : pandas.Series
        Labels column
    X : pandas.DataFrame
        Features dataframe
    BPs : int
        Number of boundary points

    Returns
    -------
    plotly.graph_objects.Figure
        The 2D RadViz figure
    """
    # Process data (same as RadViz2D function)
    y.rename("index", inplace=True)
    X = matrixNormlization(X)
    S = X  # S is the symbol matrix
    DS_names = S.columns
    X_matrix = get_X2Dmatrix(DS_names)  # X is DAs matrix
    S_hat = Radviz2DMapping(S, X_matrix)
    d = DS_names.size
    df, df_circle = Dataframe2DPreparation(S_hat, X_matrix, d, BPs, y)

    # Create figure (same logic as _2Dscatterplot_plotly.py)
    color_sequence = []
    for i in px.colors.qualitative.Plotly[1:]:
        color_sequence.append(i)
    color_sequence.append(px.colors.qualitative.Plotly[0])
    for i in px.colors.qualitative.Set2:
        color_sequence.append(i)
    for i in px.colors.qualitative.Pastel:
        color_sequence.append(i)

    df.rename(columns={'index': 'label'}, inplace=True)
    fig = go.Figure()
    fig = px.scatter(df, x=0, y=1, color="label", color_discrete_sequence=color_sequence, text='AnchorsLabel')
    fig.add_trace(go.Scatter(
        mode='markers',
        marker=dict(size=0, color=px.colors.qualitative.Plotly[0], opacity=0.1),
        x=df_circle[0], y=df_circle[1], showlegend=False
    ))
    fig.update_layout(
        dragmode='select',
        width=1000,
        height=1000,
        hovermode='closest',
        margin=dict(l=50, r=50, b=50, t=50),
        legend=dict(orientation="h", yanchor="top", y=1, xanchor="right", x=1, font=dict(size=12)),
        yaxis_title=None,
        xaxis_title=None
    )

    return fig


def generate_radviz3d_figure(y, X, BPs=10000):
    """
    Generate 3D RadViz figure (replicates plotRadviz3D logic).

    Parameters
    ----------
    y : pandas.Series
        Labels column
    X : pandas.DataFrame
        Features dataframe
    BPs : int
        Number of boundary points

    Returns
    -------
    plotly.graph_objects.Figure
        The 3D RadViz figure
    """
    # Process data (same as RadViz3D function)
    y.rename("index", inplace=True)
    X = matrixNormlization3D(X)
    S = X  # S is the symbol matrix
    DS_names = S.columns
    X_matrix = get_X3Dmatrix(DS_names)  # X is DAs matrix
    S_hat = Radviz3DMapping(S, X_matrix)
    d = DS_names.size
    df, df_sphere = Dataframe3DPreparation(S_hat, X_matrix, d, BPs, y)

    # Create figure (same logic as _3Dscatterplot_plotly.py)
    color_sequence = []
    for i in px.colors.qualitative.Plotly[1:]:
        color_sequence.append(i)
    color_sequence.append(px.colors.qualitative.Plotly[0])
    for i in px.colors.qualitative.Set2:
        color_sequence.append(i)
    for i in px.colors.qualitative.Pastel:
        color_sequence.append(i)

    df.rename(columns={'index': 'label'}, inplace=True)
    fig = go.Figure()
    fig = px.scatter_3d(df, x='x', y='y', z='z', color="label", color_discrete_sequence=color_sequence, text='AnchorsLabel')
    fig.add_trace(go.Scatter3d(
        mode='markers',
        marker=dict(size=0, color='white', opacity=0.1),
        x=df_sphere["x"], y=df_sphere["y"], z=df_sphere["z"], showlegend=False
    ))

    return fig


def generate_radviz3d_sorted_figure(y, X, BPs=10000):
    """
    Generate 3D RadViz with sorting figure.

    Parameters
    ----------
    y : pandas.Series
        Labels column
    X : pandas.DataFrame
        Features dataframe
    BPs : int
        Number of boundary points

    Returns
    -------
    plotly.graph_objects.Figure or None
        The 3D RadViz figure with sorting, or None if sorting not available
    """
    if not SORTING_AVAILABLE:
        return None

    # Process data (same as RadViz3D_withSorting function)
    y_copy = y.copy()
    y_copy.rename("index", inplace=True)

    # Normalize the data
    X = matrixNormlization3D(X)

    # Analyze correlations and group attributes
    print("  - Analyzing attribute correlations...")
    groups, numberOfAtributes = deepCorrelatorsGroups(X)

    # Prepare sorted attribute list
    sortedAttributes = []
    for i in groups:
        for e in i:
            sortedAttributes.append(e)

    # Count attributes per group
    nInEachGroup = []
    for i in groups:
        nInEachGroup.append(len(i))

    # Keep original data as S matrix
    S = X.copy()

    # Generate sorted anchors based on groups
    print("  - Generating sorted anchors...")
    X_anchors = GetSortedAnchors(np.array(nInEachGroup))

    # Prepare anchor matrix
    DAsLabel = X_anchors[['label']]
    X_anchors = X_anchors.drop(['label'], axis=1)
    X_anchors['DS_names'] = sortedAttributes
    X_anchors = X_anchors.set_index('DS_names')
    X_anchors.index.name = None

    # Reorder S matrix according to sorted attributes
    S = S[sortedAttributes]

    # Get column names
    DS_names = S.columns

    # Perform RadViz mapping
    print("  - Performing RadViz mapping...")
    S_hat = Radviz3DMapping(S, X_anchors)

    # Prepare dataframe for visualization
    d = DS_names.size
    df, df_sphere = Dataframe3DPreparation(S_hat, X_anchors, d, BPs, y_copy)

    # Create figure (same as 3D)
    color_sequence = []
    for i in px.colors.qualitative.Plotly[1:]:
        color_sequence.append(i)
    color_sequence.append(px.colors.qualitative.Plotly[0])
    for i in px.colors.qualitative.Set2:
        color_sequence.append(i)
    for i in px.colors.qualitative.Pastel:
        color_sequence.append(i)

    df.rename(columns={'index': 'label'}, inplace=True)
    fig = go.Figure()
    fig = px.scatter_3d(df, x='x', y='y', z='z', color="label", color_discrete_sequence=color_sequence, text='AnchorsLabel')
    fig.add_trace(go.Scatter3d(
        mode='markers',
        marker=dict(size=0, color='white', opacity=0.1),
        x=df_sphere["x"], y=df_sphere["y"], z=df_sphere["z"], showlegend=False
    ))

    return fig


def main():
    """Main execution function"""
    print("=" * 70)
    print("RadViz-Plotly HTML Visualization Generator")
    print("=" * 70)

    # Load dataset
    data_path = os.path.join(os.path.dirname(__file__), '..', 'tests', 'DataFolder', 'BreastCancer.csv')
    data = pd.read_csv(data_path)

    # Prepare output directory
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'iframe_figures')
    os.makedirs(output_dir, exist_ok=True)

    print(f"\nDataset: {data.shape[0]} samples, {data.shape[1]-1} features")
    print(f"Output directory: {output_dir}")
    print("\n" + "=" * 70)

    # Generate 2D RadViz
    print("\n1. Generating 2D RadViz...")
    y_2d = data['index'].copy()
    X_2d = data.drop(['index'], axis=1).copy()
    fig_2d = generate_radviz2d_figure(y_2d, X_2d, BPs=10000)
    output_2d = os.path.join(output_dir, 'BreastCancer_2D_RadViz.html')
    fig_2d.write_html(output_2d)
    file_size_2d = os.path.getsize(output_2d) / (1024 * 1024)  # MB
    print(f"   ✓ Saved to: {output_2d}")
    print(f"   ✓ File size: {file_size_2d:.2f} MB")

    # Generate 3D RadViz
    print("\n2. Generating 3D RadViz...")
    y_3d = data['index'].copy()
    X_3d = data.drop(['index'], axis=1).copy()
    fig_3d = generate_radviz3d_figure(y_3d, X_3d, BPs=10000)
    output_3d = os.path.join(output_dir, 'BreastCancer_3D_RadViz.html')
    fig_3d.write_html(output_3d)
    file_size_3d = os.path.getsize(output_3d) / (1024 * 1024)  # MB
    print(f"   ✓ Saved to: {output_3d}")
    print(f"   ✓ File size: {file_size_3d:.2f} MB")

    # Generate 3D RadViz with Sorting
    if SORTING_AVAILABLE:
        print("\n3. Generating 3D RadViz with Sorting...")
        y_sorted = data['index'].copy()
        X_sorted = data.drop(['index'], axis=1).copy()
        fig_sorted = generate_radviz3d_sorted_figure(y_sorted, X_sorted, BPs=10000)
        if fig_sorted:
            output_sorted = os.path.join(output_dir, 'BreastCancer_3D_RadViz_Sorted.html')
            fig_sorted.write_html(output_sorted)
            file_size_sorted = os.path.getsize(output_sorted) / (1024 * 1024)  # MB
            print(f"   ✓ Saved to: {output_sorted}")
            print(f"   ✓ File size: {file_size_sorted:.2f} MB")
    else:
        print("\n3. Skipping 3D with Sorting (dependencies not installed)")
        print("   Install with: pip install scikit-learn transformations")

    print("\n" + "=" * 70)
    print("✓ All visualizations generated successfully!")
    print("=" * 70)
    print(f"\nHTML files saved to: {output_dir}")
    print("\nTo view them:")
    print("1. Commit and push to GitHub")
    print("2. Use links like:")
    print("   https://htmlpreview.github.io/?https://github.com/elewah/RadViz-Plotly/blob/master/iframe_figures/FILENAME.html")
    print("=" * 70)


if __name__ == "__main__":
    main()
