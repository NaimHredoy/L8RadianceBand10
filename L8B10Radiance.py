# Import system modules

import arcpy
from arcpy import env

# set environment
# Here you have to set your own directory

env.workspace="H:/STUDY/Document/Papers/RS02/aaaaaaa"
env.overwriteOutput=True
from arcpy.sa import *

# Checking out spatial extension 

arcpy.CheckOutExtension("Spatial")

# Setting up variables

image = arcpy.Raster("H:/STUDY/Document/Papers/RS02/aaaaaaa/LC08_L1TP_138043_20160411_20170326_01_T1_B10.TIF")
cons1 = 0.0003342
cons2 = 0.1

# performing main operation

init = image * cons1
R=init+cons2

# Save the output

R.save("H:/STUDY/Document/Papers/RS02/aaaaaaa/rad.tif")
