######################################################################
## AddLayerToMxd.py
## 
## Adds new layer to the map document at specified position
######################################################################

import arcpy

mxDoc = "C:/Student/PYTH/CityBase.mxd"
# Add a new layer to the map document
# mxDoc points to the map document object
# df points to the first dataframe
lyrToAdd = arcpy.mapping.Layer(r"C:\Student\Database\BikeTrails.lyr")
# Locate existing layer for placement position
referenceLyr = arcpy.mapping.ListLayers(mxDoc, "ROW", df)[0]
# Add layer to map document
arcpy.mapping.AddLayer( df, lyrToAdd)
# Move new layer to position above reference layer
arcpy.mapping.MoveLayer(df, referenceLyr, lyrToAdd, "BEFORE")