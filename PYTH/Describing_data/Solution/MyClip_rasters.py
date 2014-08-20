##------------------------------------------------------------------------------
## Name:        MyClip_rasters.py
## Purpose:
##
## Author:      Student
##
## Created:     May 22, 2013
## Copyright:   (c) Esri Student 2013
##------------------------------------------------------------------------------

import arcpy
arcpy.env.workspace = r"C:\Student\PYTH\Describing_data\Tahoe\All"

desc = arcpy.Describe("C:\Student\PYTH\Describing_data\Tahoe\Emer\erelev")
rasExtent = desc.extent
ras_List = arcpy.ListRasters()

for name in ras_List:
    arcpy.Clip_management(name, str(rasExtent), "{}_clip".format(name))

#Alternate way to acces the Clip_management geoprocessing tool is to
# specify the toolbox alias and them the name in the form of:
# arcpy.<toolbox alias>.<toolname>()
# Alternate code for line 19 above is:
#arcpy.management.Clip(name, str(rasExtent), "{}_clip".format(name))

print "Script completed"
