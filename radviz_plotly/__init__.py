# File: radviz_plotly/__init__.py
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 23:07:51 2020

@author: elewah
"""

from .RadViz2D import RadViz2D
from .RadViz3D import RadViz3D

# Import sorting version if dependencies are available
try:
    from .RadViz3DSort import RadViz3D_withSorting
    __all__ = ['RadViz2D', 'RadViz3D', 'RadViz3D_withSorting']
except ImportError as e:
    print(f"Warning: RadViz3D_withSorting not available. Install sklearn and transformations to use it.")
    __all__ = ['RadViz2D', 'RadViz3D']