######################################################################
## ListLayerNames.py
## 
## List layer names in the first dataframe
######################################################################

import arcpy

mxDoc = "C:/Student/PYTH/CityBase.mxd"
# List layer names in first dataframe
# mxDoc points to map document
df = arcpy.mapping.ListDataFrames(mxDoc)[0]
lstLyrs = arcpy.mapping.ListLayers(mxDoc, "*", df)
for lyr in lstLyrs:
     print lyr.name