import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap
import sys
# Call the file name
FILE_NAME = ("S5P_RPRO_L2__NO2____20210519T120445_20210519T134615_18644_03_020400_20221107T225019.nc")
file = Dataset(FILE_NAME, 'r')
# Read the data
ds = file
grp = 'PRODUCT'
lat = ds.groups[grp].variables['latitude'][0][:][:]
lon = ds.groups[grp].variables['longitude'][0][:][:]
if 'NO2' in FILE_NAME:
    sds_name = 'nitrogendioxide_tropospheric_column'
    map_label = 'mol/m2'
elif 'AER_AI' in FILE_NAME:
    sds_name = 'aerosol_index_354_388'
    map_label = 'Aerosol Index'
else:
    print("Unknown file type. Exiting.")
    sys.exit()
data = ds.groups[grp].variables[sds_name]
print(ds.groups[grp].variables.keys())
# Get necessary attributes
fv = data._FillValue
# Get lat and lon information
min_lat = np.min(lat)
max_lat = np.max(lat)
min_lon = np.min(lon)
max_lon = np.max(lon)
# Get the data as an array and mask fill/missing values
dataArray = np.array(data[0][:][:])
dataArray[dataArray == fv] = np.nan
data = np.ma.masked_array(dataArray, np.isnan(dataArray))
# Get statistics
average = np.nanmean(dataArray)
stdev = np.nanstd(dataArray)
median = np.nanmedian(dataArray)
# Print statistics
print(f'The average of this data is: {average:.2e}')
print(f'The standard deviation is: {stdev:.2e}')
print(f'The median is: {median:.2e}')
print(f'The range of latitude in this file is: {min_lat} to {max_lat} degrees')
print(f'The range of longitude in this file is: {min_lon} to {max_lon} degrees')
# Ask user if they want to plot the data
is_map = input('\nWould you like to create a map of this data? (Y/N) ').strip().lower()
if is_map == 'y':
    plt.figure(figsize=(10, 6))  # Adjust figure size for Spyder
    m = Basemap(projection='cyl', resolution='l',
                llcrnrlat=-35, urcrnrlat=0,
                llcrnrlon=0, urcrnrlon=45)
    m.drawcoastlines(linewidth=0.5)
    m.drawparallels(np.arange(-90., 120., 30.), labels=[1, 0, 0, 0])
    m.drawmeridians(np.arange(-180, 180., 45.), labels=[0, 0, 0, 1])
    my_cmap = plt.cm.get_cmap('jet')
    my_cmap.set_under('w')
    vmin1 = 0.0
    vmax1 = np.nanmax(data) * 0.05  # Adjust scaling factor
    m.pcolormesh(lon, lat, data, latlon=True, vmin=vmin1, vmax=vmax1, cmap=my_cmap)
    cb = m.colorbar()
    cb.set_label(map_label)
    #plt.title(f'{FILE_NAME}\n {data.long_name}')
    fig = plt.gcf()
    plt.show()
    # Ask user if they want to save the map
    is_save = input('\nWould you like to save this map? (Y/N) ').strip().lower()
    if is_save == 'y':
        pngfile = f'{FILE_NAME[:-3]}.png'
        fig.savefig(pngfile, dpi=300)
        print(f"Map saved as {pngfile}")
# Close the file
file.close()
print("Script execution complete.")