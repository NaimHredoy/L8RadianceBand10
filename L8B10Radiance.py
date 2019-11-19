import arcpy
from arcpy import env
env.workspace="H:/STUDY/Document/Papers/RS02/aaaaaaa"
env.overwriteOutput=True
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")

image = arcpy.Raster("H:/STUDY/Document/Papers/RS02/aaaaaaa/LC08_L1TP_138043_20160411_20170326_01_T1_B10.TIF")
cons1 = 0.0003342
cons2 = 0.1

init = image * cons1
R=init+cons2

R.save("H:/STUDY/Document/Papers/RS02/aaaaaaa/rad.tif")
