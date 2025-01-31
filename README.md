Description
This project processes and visualizes Nitrogen Dioxide (NO2) measurements from the Sentinel-5 Precursor (S5P) mission. It extracts data from NetCDF files, performs statistical analysis (average, standard deviation, and median), and offers an option to plot and save maps using Basemap.

Features
Extracts and analyzes NO2 or aerosol index data.
Provides statistical insights (average, std dev, median).
Plots the data on a world map.
Saves the map as a PNG file.
Requirements
Python 3.x
Libraries: xarray, numpy, matplotlib, netCDF4, basemap
Installation
Install the necessary libraries via pip:

bash
Copy
pip install xarray numpy matplotlib netCDF4 basemap
Usage
Set the FILE_NAME variable to your NetCDF file.
Run the script:
bash
Copy
python s5p_data_analysis.py
Optionally, visualize and save the map.
