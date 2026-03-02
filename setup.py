import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RadViz-Plotly",
    version="0.3.0",
    author="Elewah",
    author_email="abdelrahman.elewah@gmail.com",
    description="2D and 3D RadViz library with attribute sorting, using Plotly scatter plots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elewah/RadViz-Plotly.git",
    packages=setuptools.find_packages(),
    install_requires=[
        'plotly>=4.0.0',
        'pandas>=1.0.0',
        'numpy>=1.18.0',
        'scikit-learn>=0.24.0',
        'transformations>=2020.1.1',
    ],
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'black>=23.0.0',
            'flake8>=6.0.0',
            'isort>=5.12.0',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    python_requires='>=3.8',
    project_urls={
        'Bug Reports': 'https://github.com/elewah/RadViz-Plotly/issues',
        'Source': 'https://github.com/elewah/RadViz-Plotly',
    },
)