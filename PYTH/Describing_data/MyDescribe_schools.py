#-------------------------------------------------------------------------------
# Name:        MyDescribe_schools.py
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
desc = arcpy.Describe('Schools')
print "Name: {} shape: {} Type: {}".format (desc.name, desc.shapeType, desc.datasetType)
for fld in desc.fields:
    print "\t{}".format(fld.name)

descGDB = arcpy.Describe(arcpy.env.workspace)
print "workspace type: {} release number: {} file path: {}".format(descGDB.workspaceType, descGDB.release, descGDB.path)
print "Script completed"