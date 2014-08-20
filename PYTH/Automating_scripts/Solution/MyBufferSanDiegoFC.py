##------------------------------------------------------------------------------
## Name:        MyBufferSanDiegoFC.py
## Purpose:     This script buffers points by 1000 ft, polygons by -750 ft,
##              and polylines by 500 ft, using the shapeType Describe property
##              from each feature class in SanDiego.gdb
##
## Author:      Student
##
## Created:     May 23, 2013
## Copyright:   (c) Esri Student 2013
##------------------------------------------------------------------------------

import arcpy
arcpy.env.workspace = "C:/Student/PYTH/Automating_scripts/Solution/SanDiego.gdb"

fc_list = arcpy.ListFeatureClasses()
for featClass in fc_list:
    desc = arcpy.Describe(featClass)
    if desc.shapeType == "Point":
        buffDist = '1000 feet'
    elif desc.shapeType == "Polyline":
        buffDist = '500 feet'
    elif desc.shapeType == "Polygon":
        buffDist = '-750 feet'
    arcpy.Buffer_analysis(in_features = featClass,
                    out_feature_class = featClass + "_Buff",
                    buffer_distance_or_field = buffDist)

print "Script completed"
