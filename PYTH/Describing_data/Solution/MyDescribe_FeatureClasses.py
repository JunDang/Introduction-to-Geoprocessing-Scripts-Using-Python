##------------------------------------------------------------------------------
## Name:        MyDescribe_FeatureClasses.py
## Purpose:
##
## Author:      Student
##
## Created:     May 22, 2013
## Copyright:   (c) Esri Student 2013
##------------------------------------------------------------------------------

import arcpy
arcpy.env.workspace = r"C:\Student\PYTH\Describing_data\Corvallis.gdb"

fc_list = arcpy.ListFeatureClasses()
for name in fc_list:
    desc = arcpy.Describe(name)
    featCount = arcpy.GetCount_management(name)
    print "Name: {} Shape: {} SR: {} Count: {}".format(
        desc.name, desc.shapeType, desc.spatialReference.name, featCount)

print "Script completed"