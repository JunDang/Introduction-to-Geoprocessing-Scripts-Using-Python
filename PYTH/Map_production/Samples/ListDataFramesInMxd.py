######################################################################
## ListDataFramesInMxd.py
## 
## Lists the names of the first dataframes in an mxd
######################################################################

import arcpy

mxDoc = "C:/Student/PYTH/CityBase.mxd"
# List first dataframe name in map document
# mxDoc points to map document
df = arcpy.mapping.ListDataFrames(mxDoc)[0]
print df.name