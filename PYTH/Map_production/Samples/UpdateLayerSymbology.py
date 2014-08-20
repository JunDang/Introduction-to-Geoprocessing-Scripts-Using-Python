######################################################################
## UpdateLayerSymbology.py
## 
## Applies layer file symbology to specified layer
######################################################################

import arcpy

mxDoc = "C:/Student/PYTH/CityBase.mxd"
# Update specified layer symbology from .lyr file
# mxDoc points to map document object
# df points to first dataframe
df = arcpy.mapping.ListDataFrames(mxDoc)[0]
lyrToUpdate = arcpy.mapping.ListLayers(df,"ParkingMeters")[0]
symbologyLyr = arcpy.mapping.Layer(r"C:\Student\PYTH\MeterSym.lyr")
arcpy.mapping.UpdateLayer(df, lyrToUpdate, symbologyLyr, True)