# RadViz-Plotly

<table>
    <tr>
        <td>Latest Release</td>
        <td>
            <a href="https://pypi.org/project/RadViz-Plotly/">
            <img src="https://badge.fury.io/py/RadViz-Plotly.svg" alt="PyPI version badge"/>
            </a>
        </td>
    </tr>
    <tr>
        <td>Examples</td>
        <td>
            <a href="https://mybinder.org/v2/gh/elewah/RadViz-Plotly-Examples/master">
            <img src="https://img.shields.io/badge/Jupyter--Lab-Examples-orange" alt="Jupyter Lab Examples badge"/>
            </a>
        </td>
    </tr>
    <tr>
        <td>PyPI Downloads</td>
        <td>
            <a href="https://pepy.tech/project/RadViz-Plotly">
            <img src="https://pepy.tech/badge/RadViz-Plotly" alt="PyPI Downloads badge"/>
            </a>
        </td>
    </tr>
    <tr>
        <td>License</td>
        <td>
            <a href="https://opensource.org/licenses/MIT">
            <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License badge"/>
            </a>
        </td>
    </tr>
</table>

## Overview
RadViz-Plotly is an open-source Python package designed for data scientists to create 2D and 3D Radial Visualization (RadViz) plots for high-dimensional datasets. These visualizations provide a comprehensive view of data distribution across dimensions, enabling better understanding and discovery of hidden insights. The package leverages the powerful interactive tools of the Plotly library.

### Key Features
- **2DRadViz**: Generates 2D Radial Visualizations.
- **3DRadViz**: Creates 3D Radial Visualizations.
- **Interactive Visualizations**: Zoom, filter labels, and rotate 3D graphs.

## Quickstart

### Without Local Installation
You can try RadViz-Plotly without installing it locally by following these steps:

1. Click [here](https://mybinder.org/v2/gh/elewah/RadViz-Plotly-Examples/master) to access interactive Jupyter notebooks. This repository contains three folders, each with datasets and a Jupyter notebook demonstrating RadViz-Plotly.
   - **Note**: The Jupyter environment may take some time to load.
2. Open one of the folders (e.g., Car Evaluation Dataset, Election Dataset, or Iris Dataset).
3. Open the file with the `.ipynb` extension (Jupyter notebook).
4. From the **Cell** menu in the toolbar, select **Run All** to execute the notebook.

**Hints:**
- The first run may take time to install dependencies.
- The package supports interactive features like zooming, filtering labels, and rotating 3D graphs.
- RadViz-Plotly depends on the [Plotly](https://plot.ly/python) library.

### With Local Installation

1. Install RadViz-Plotly using pip:
   ```bash
   pip install RadViz-Plotly
   ```
2. Clone the examples repository:
   ```bash
   git clone https://github.com/elewah/RadViz-Plotly-Examples.git
   ```
   Alternatively, download the repository as a ZIP file [here](https://github.com/elewah/RadViz-Plotly-Examples/archive/master.zip).
3. Run the examples using Jupyter Lab to understand how to use the RadViz-Plotly package.

## Gallery

<p align="center">
<img src="https://elewah.github.io/RadViz-Plotly/image/3D-1.gif" width="400" alt="3D RadViz Example 1">
<img src="https://elewah.github.io/RadViz-Plotly/image/3D-2.gif" width="400" alt="3D RadViz Example 2">
<img src="https://elewah.github.io/RadViz-Plotly/image/Slide3.PNG" width="400" alt="2D RadViz Example">
<img src="https://elewah.github.io/RadViz-Plotly/image/Slide2.PNG" width="400" alt="3D RadViz Example">
</p>

## About
RadViz-Plotly was developed by a research group at the IoT Lab, Ontario Tech University. It provides tools for creating 2D and 3D Radial Visualizations, enabling data scientists to explore high-dimensional datasets interactively.

## Citation
If you use RadViz-Plotly in your research, please cite the following paper:

[A. Elewah, A. A. Badawi, H. Khalil, S. Rahnamayan, and K. Elgazzar, "3D-RadViz: Three Dimensional Radial Visualization for Large-Scale Data Visualization," 2021 IEEE Congress on Evolutionary Computation (CEC), 2021, pp. 1037-1046, doi: 10.1109/CEC45853.2021.9504983.](https://ieeexplore.ieee.org/document/9504983)


## License
This project is licensed under the [MIT License](LICENSE).

<div style="display:flex; justify-content: center;">
<a href="https://ontariotechu.ca/">
<img src="https://elewah.github.io/RadViz-Plotly/image/ontariotechu-log.jpg" alt="Ontario Tech University Logo" width="250">
</a>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://iotresearchlab.ca/">
<img src="https://elewah.github.io/RadViz-Plotly/image/IoT-lab.png" width="300" alt="IoT Lab Logo">
</a>
</div>


