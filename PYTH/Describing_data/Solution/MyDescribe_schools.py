##------------------------------------------------------------------------------
## Name:        MyDescribe_schools.py
## Purpose:
##
## Author:      Student
##
## Created:     May 22, 2013
## Copyright:   (c) Esri Student 2013
##------------------------------------------------------------------------------

import arcpy
arcpy.env.workspace = r"C:\Student\PYTH\Describing_data\Corvallis.gdb"

desc = arcpy.Describe('Schools')
print "Name: {} Shape: {} Type: {}".format(desc.name, desc.shapeType,
                                            desc.datasetType)

print "Field names"
for fld in desc.fields:
    print "\t{}".format(fld.name)

descGDB = arcpy.Describe(arcpy.env.workspace)
print "GDB Type: {} Release: {} Path: {}".format(
    descGDB.workspaceType, descGDB.release, descGDB.path)

print "Script completed"