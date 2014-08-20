#-------------------------------------------------------------------------------
# Name:       PyScripter
# Purpose:
#
# Author:      Jun Dang
#
# Created:     19/08/2014
# Copyright:   (c) Jun Dang 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy
arcpy.env.workspace = "C:\Student\PYTH\Describing_data\Corvallis.gdb"
fc_list = arcpy.ListFeatureClasses()
for name in fc_list:
    desc = arcpy.Describe(name)
    featCount = arcpy.GetCount_management(name)
    print "Name: {} shape: {} SR: {} Count: {}".format(desc.name, desc.shapeType, desc.spatialReference.name, featCount)
print "Script completed"

