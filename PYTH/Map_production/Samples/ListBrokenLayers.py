######################################################################
## ListBrokenLayers.py
## 
## List all of the broken layers in a map document
######################################################################

import arcpy
import os.path

mxDoc = "C:/Student/PYTH/CityBase.mxd"
# List all layers with broken data sources in mxd
# mxDoc points to map document object
brokenLyrs = arcpy.mapping.ListBrokenDataSources(mxDoc)
print "MXD file: " + os.path.basename(mxDoc.filePath)
for lyr in brokenLyrs:
     print  "\t" + lyr.name