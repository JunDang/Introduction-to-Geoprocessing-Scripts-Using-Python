#-------------------------------------------------------------------------------
# Name:        MyBufferSandiegoFC.py
# Purpose:
#
# Author:      Jun Dang
#
# Created:     19/08/2014
# Copyright:   (c) Jun Dang 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy
arcpy.env.workspace = "C:\Student\PYTH\Automating_scripts\SanDiego.gdb"
fc_list = arcpy.ListFeatureClasses()
for featClass in fc_list:
    desc = arcpy.Describe(featClass)
    if desc.shapeType == 'Point':
        buffDist = '1000 feet'
    elif desc.shapeType == 'Polyline':
        buffDist = '500 feet'
    elif desc.shapeType == 'Polygon':
        buffDist = '-750 feet'
    arcpy.Buffer_analysis(in_features = featClass, out_feature_class = featClass + "_Buff", buffer_distance_or_field = buffDist)
print "Script completed"