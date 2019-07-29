# ---
# jupyter:
#   jupytext:
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
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#Reading-the-geolocation-data" data-toc-modified-id="Reading-the-geolocation-data-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Reading the geolocation data</a></span></li><li><span><a href="#Check-the-metadata-with-hdf4ls" data-toc-modified-id="Check-the-metadata-with-hdf4ls-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Check the metadata with hdf4ls</a></span></li><li><span><a href="#Read-the-CoreMetadata.0-attribute-with-parseMeta" data-toc-modified-id="Read-the-CoreMetadata.0-attribute-with-parseMeta-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Read the CoreMetadata.0 attribute with parseMeta</a></span></li><li><span><a href="#Plotting-the-lats-and-lons" data-toc-modified-id="Plotting-the-lats-and-lons-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Plotting the lats and lons</a></span></li></ul></div>

# %%
from pathlib import Path
from pyhdf.SD import SD, SDC
from matplotlib import pyplot as plt
import context

# %% [markdown]
# # Introduction
#
# This notebook shows how to use:
#
# * [hdf4ls](https://github.com/phaustin/a301_code/blob/master/a301/scripts/hdf4ls.py) to
#   list the contents of an hdf4 Modis file
#   
# * [modismeta_read](https://github.com/phaustin/a301_code/blob/master/a301/scripts/modismeta_read.py) to print
#   some of the metadata of an hdf4 Modis file
#   
# You'll need to download the MYD03 lat/lon file from LAADSweb that corresponds to your
# MYD02 level1b granule

# %% [markdown]
# # Reading the geolocation data
#
# I downloaded a lat/lon MYD03 file from LAADSweb.  This contains the center lat and longitude
# of every pixel at 1 km resolution.

# %%
#Path.cwd finds the "current working directory", i.e. the directory holding this notebook.
this_dir=Path.cwd()
#move up one one folder and down to data
data_dir = this_dir.parent / Path('data')
hdf_files=list(data_dir.glob("MYD03*2110*.hdf"))
print(hdf_files)

# %%
read_data=True
if read_data:
    filename="MYD03.A2013222.2105.006.2013223155808.hdf"
    from a301.utils.data_read import download
    download(filename)
    local_file = Path.cwd() / Path(filename)
    to_file = data_dir / Path(filename)
    local_file.rename(to_file)

# %% [markdown]
# # Check the metadata with hdf4ls

# %%
from a301.scripts.hdf4ls import hdf4ls
help(hdf4ls)

# %%
hdf4ls(hdf_files[0])

# %% [markdown]
# # Read the CoreMetadata.0 attribute with parseMeta

# %%
from a301.scripts.modismeta_read import parseMeta
help(parseMeta)

# %%
parseMeta(hdf_files[0])

# %% [markdown]
# # Plotting the lats and lons

# %%
the_file = SD(str(hdf_files[0]), SDC.READ)
lat_data = the_file.select('Latitude')
lon_data = the_file.select('Longitude')

# %%
fig,ax = plt.subplots(1,1,figsize = (10,14))
ax.plot(lon_data[900:940,900:940],lat_data[900:940,900:940],'b+');
ax.set(xlabel='longitude (deg W)',ylabel='latitude (deg N)');

# %% [markdown]
# **Note two things:  1) the pixels overlap and 2) they don't line up on lines of constant longitude and latitude**
#
# **The pixels are also not all the same size -- this distortion is called the [bowtie effect](http://eoweb.dlr.de:8080/short_guide/D-MODIS.html)**

# %%
