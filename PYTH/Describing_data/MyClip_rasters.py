#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jun Dang
#
# Created:     19/08/2014
# Copyright:   (c) Jun Dang 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy
arcpy.env.workspace = "C:\Student\PYTH\Describing_data\Tahoe\All"
desc = arcpy.Describe("C:\Student\PYTH\Describing_data\Tahoe\Emer\erelev")
rasExtent = desc.extent
ras_list = arcpy.ListRasters()
for name in ras_list:
     arcpy.Clip_management(name, str(rasExtent), '{}_clip'.format(name))
print "Script completed"