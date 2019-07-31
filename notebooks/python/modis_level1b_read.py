# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.2.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown] {"toc": true}
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Reading-modis-data" data-toc-modified-id="Reading-modis-data-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Reading modis data</a></span><ul class="toc-item"><li><span><a href="#Installing-pyhdf" data-toc-modified-id="Installing-pyhdf-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Installing pyhdf</a></span></li><li><span><a href="#Downloading-the-data-and-reading-the-file" data-toc-modified-id="Downloading-the-data-and-reading-the-file-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Downloading the data and reading the file</a></span></li><li><span><a href="#Navigating-the-file-system" data-toc-modified-id="Navigating-the-file-system-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Navigating the file system</a></span></li><li><span><a href="#Using-pydf-to-get-metadata" data-toc-modified-id="Using-pydf-to-get-metadata-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Using pydf to get metadata</a></span></li><li><span><a href="#Find-all-the-datasets-using-pyhdf.SD.datasets()" data-toc-modified-id="Find-all-the-datasets-using-pyhdf.SD.datasets()-2.5"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Find all the datasets using pyhdf.SD.datasets()</a></span></li><li><span><a href="#open-one-of-the-datasets-(number-4,-EV_1KM_Emissive)-and-get-its-shape-and-data-type" data-toc-modified-id="open-one-of-the-datasets-(number-4,-EV_1KM_Emissive)-and-get-its-shape-and-data-type-2.6"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>open one of the datasets (number 4, EV_1KM_Emissive) and get its shape and data type</a></span></li><li><span><a href="#Get-the-first-row-of-the-first-channel-and-find-its-numpy-dtype" data-toc-modified-id="Get-the-first-row-of-the-first-channel-and-find-its-numpy-dtype-2.7"><span class="toc-item-num">2.7&nbsp;&nbsp;</span>Get the first row of the first channel and find its numpy dtype</a></span></li><li><span><a href="#get-all-the-rows-and-columns-for-the-first-channel" data-toc-modified-id="get-all-the-rows-and-columns-for-the-first-channel-2.8"><span class="toc-item-num">2.8&nbsp;&nbsp;</span>get all the rows and columns for the first channel</a></span></li><li><span><a href="#Find-the-attributes-for-EV_1KM_Emissive" data-toc-modified-id="Find-the-attributes-for-EV_1KM_Emissive-2.9"><span class="toc-item-num">2.9&nbsp;&nbsp;</span>Find the attributes for EV_1KM_Emissive</a></span></li><li><span><a href="#Print-the-first-1000-characters-of-the-Metadata.0-string" data-toc-modified-id="Print-the-first-1000-characters-of-the-Metadata.0-string-2.10"><span class="toc-item-num">2.10&nbsp;&nbsp;</span>Print the first 1000 characters of the Metadata.0 string</a></span></li></ul></li><li><span><a href="#Now-plot-the-data-using-imshow" data-toc-modified-id="Now-plot-the-data-using-imshow-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Now plot the data using imshow</a></span><ul class="toc-item"><li><span><a href="#find-the-index-for-channel-30" data-toc-modified-id="find-the-index-for-channel-30-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>find the index for channel 30</a></span></li><li><span><a href="#Let-python-figure-this-out" data-toc-modified-id="Let-python-figure-this-out-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Let python figure this out</a></span></li><li><span><a href="#Read-channel-30-at-index-9-into-a-numpy-array-of-type-uint16" data-toc-modified-id="Read-channel-30-at-index-9-into-a-numpy-array-of-type-uint16-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Read channel 30 at index 9 into a numpy array of type uint16</a></span></li><li><span><a href="#Plot-the-channel-30-image" data-toc-modified-id="Plot-the-channel-30-image-3.4"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>Plot the channel 30 image</a></span></li></ul></li><li><span><a href="#For-Wednesday-(don't-need-to-hand-in)" data-toc-modified-id="For-Wednesday-(don't-need-to-hand-in)-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>For Wednesday (don't need to hand in)</a></span></li><li><span><a href="#Write-the-calibrated-channel-out-for-safekeeping" data-toc-modified-id="Write-the-calibrated-channel-out-for-safekeeping-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Write the calibrated channel out for safekeeping</a></span></li><li><span><a href="#Move-the-file-to-data_dir" data-toc-modified-id="Move-the-file-to-data_dir-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Move the file to data_dir</a></span></li></ul></div>

# %%
from pathlib import Path
from pyhdf.SD import SD, SDC
import pprint
import numpy as np
from matplotlib import pyplot as plt
import context
# %%
from pathlib import Path
print(Path().resolve())
import context
# %% [markdown]
# # Introduction
#
# This notebook assumes that you have gone to the LAADS DAAC archive and downloaded a Modis Level1b 5 minute granule from the Aqua satellite (a MYD021KM hdf file).  Below we use the pyhdf module to read a single channel (channel 30) centered at 9.7 microns according to [the Modis channel listing](https://modis.gsfc.nasa.gov/about/specifications.php).  We plot the raw counts from that channel using the 
# [matplotlib imshow](https://matplotlib.org/examples/images_contours_and_fields/image_demo.html) function to display the raw image
#
# If you don't have a MYD021KM file you can grab mine by changing
#
#      get_data=False
#   
# to True in the next cell.
#      
#      

# %%
modis_files= list(context.data_dir.glob("*hdf"))
print(list(modis_files))

# %% [markdown]
# # Reading modis data

# %% [markdown]
# A better choice would be someplace within the a301 folder tree.  I know this notebook is
# in the tree, so I can create a new folder called a301_code/data, and since I know I am
# currently in a301/notebooks, I can find it like this:

# %% [markdown]
# ## Using pydf to get metadata
#
# I can convert the filename from a Path object to a string object and pass it to pyhdf.SD
# to find out how many datasets and attributes there are in the file
#
# In the cell below I use [f-strings](https://realpython.com/python-f-strings/) to simplify the print command,
# and split the string up across multiple lines by enclosing it in a tuple.  This works because
# when python sees that the individual lines aren't separated by a comma, it concatenates them together.
# The character \n means "newline"
#
# Note that I need to construct the full path to the data file so pyhdf can find it. pyhdf was
# written before pathlib (which was introduced in python 3.5), 
# so I need to convert the Path object to a simple string using str()

# %%
file_name = str(modis_files[0])
print(f'reading {file_name}')
the_file = SD(file_name, SDC.READ)
stars='*'*50
print((f'\n{stars}\nnumber of datasets, number of attributes'
       f'={the_file.info()}\n{stars}\n'
       f'\nHere is the help file for the info funtion:\n'))
help(SD.info)

# %% [markdown]
# ## Find all the datasets using pyhdf.SD.datasets()
#
# The datasets method creates a dictionary holding pointers to the 31 datasets.
# List them below:

# %%
the_file.attributes()

# %%
datasets_dict = the_file.datasets()

for idx,sds in enumerate(datasets_dict.keys()):
    print(idx,sds)

# %%
lat_5km = the_file.select('Latitude') # select sds
lon_5km = the_file.select('Longitude') # select sds
print(lat_5km.info())
print(help(lat_5km.info))
lat_5km=lat_5km[:,:]
lon_5km=lon_5km[:,:]

# %% [markdown]
# ## get the coase 5km lat/lons

# %%
import geotiepoints
lons_1km, lats_1km = geotiepoints.modis5kmto1km(lon_5km, lat_5km)

# %% [markdown]
# ## Interpolate to 1 km using geotiepoints
#
# Use https://python-geotiepoints.readthedocs.io/en/latest/

# %%
lons_1km.shape

# %% [markdown]
# ## open one of the datasets (EV_1KM_Emissive) and get its shape and data type

# %%
longwave_data = the_file.select('EV_1KM_Emissive') # select sds
print(longwave_data.info())

# %% [markdown]
# ## Get the first row of the first channel and find its numpy dtype
#
# (unit16 is "unsigned 16 bit integer", which is how the modis raw counts are stored)

# %%
data_row = longwave_data[0,0,:] # get sds data
print(data_row.shape,data_row.dtype)

# %% [markdown]
# ## get all the rows and columns for the first channel

# %%
longwave_data[0,:,:]

# %% [markdown]
# ## Find the attributes for EV_1KM_Emissive

# %%
pprint.pprint(longwave_data.attributes() )

# %% [markdown]
# ## Print the first 100 characters of the CoreMetadata.0 string
#
# Date, orbit number, etc. are stored in a long string attribute called 'StructMetadata.0'.  The \t character is a tab stop.

# %%
pprint.pprint(the_file.attributes()['CoreMetadata.0'][:100])

# %% [markdown]
# ## Turn the metadata into a dictionary

# %%
# read the file
import satlib.modismeta_read as modisread
meta_string=the_file.attributes()['CoreMetadata.0']
meta_dict = modisread.read_mda(meta_string)
print(meta_dict)
# %% [markdown]
# ## Get the wavelength ranges for the bands

# %%
longwave_bands = longwave_data.attributes()['band_names']
band_list=longwave_bands.split(',')
band_list

# %%
from satlib.modis_chans import chan_dict
for channum in band_list:
    print(chan_dict[channum])

# %% [markdown]
# ## Calibrate channel 21

# %%
scales=longwave_data.attributes()['radiance_scales']
offsets=longwave_data.attributes()['radiance_offsets']
scales, offsets

# %%
fig,ax = plt.subplots(1,1,figsize = (10,14))
CS=ax.imshow(ch30_data)
cax=fig.colorbar(CS)
ax.set_title('uncalibrated counts')
#
# add a label to the colorbar and flip it around 270 degrees
#
out=cax.ax.set_ylabel('Chan 30 raw counts')
out.set_verticalalignment('bottom')
out.set_rotation(270)
print(ch30_data.shape)

# %% [markdown]
# # For Wednesday (don't need to hand in)
#
# To turn the raw counts into pixel radiances, you need to apply equation 5.8 on p. 36 of the 
# [modis users guide](https://www.dropbox.com/s/ckd3dv4n7nxc9p0/modis_users_guide.pdf?dl=0):
#
# $Radiances = (RawData - offset) \times scale$
#
# We have just read the RawData,  the offset and the scale are stored in two vectors that are attributes of the Emissive dataset.  Make a version of the figure above, but plot Channel 30 radiance (in W/m^2/micron/sr), rather than raw counts.
#
# Hint:  Here is how you get the scale and offset for Channel 30.
#
#
#

# %%
ch30_calibrated =(ch30_data - ch30_offset)*ch30_scale

# %%
fig,ax = plt.subplots(1,1,figsize = (10,14))
CS=ax.imshow(ch30_calibrated)
cax=fig.colorbar(CS)
ax.set_title('Channel 30 radiance')
#
# add a label to the colorbar and flip it around 270 degrees
#
out=cax.ax.set_ylabel('Chan radiance $(W\,m^{-2}\,\mu m^{-1}\,sr^{-1})$')
out.set_verticalalignment('bottom')
out.set_rotation(270)
ch30_calibrated.shape

# %% [markdown]
# # Write the calibrated channel out for safekeeping
#
# Follow the example here: https://hdfeos.org/software/pyhdf.php

# %%
# Create an HDF file
outname="ch30_out.hdf"
sd = SD(outname, SDC.WRITE | SDC.CREATE)

# Create a dataset
sds = sd.create("ch30", SDC.FLOAT64, ch30_calibrated.shape)

# Fill the dataset with a fill value
sds.setfillvalue(0)

# Set dimension names
dim1 = sds.dim(0)
dim1.setname("row")
dim2 = sds.dim(1)
dim2.setname("col")

# Assign an attribute to the dataset
sds.units = "W/m^2/micron/sr"

# Write data
sds[:,:] = ch30_calibrated

# Close the dataset
sds.endaccess()

# Flush and close the HDF file
sd.end()

# %%
# !ls

# %% [markdown]
# # Move the file to data_dir

# %%
local_file = Path.cwd() / Path(outname)
to_file = data_dir / Path(outname)
local_file.rename(to_file)

# %%
