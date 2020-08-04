import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RadViz-Plotly", # Replace with your own username
    version="0.0.1",
    author="Elewah",
    author_email="abdelrahman.elewah@gmail.com",
    description="2D and 3D RadViz library, using plotly 2D and 3D scatter plot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elewah/RadViz-Plotly.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
