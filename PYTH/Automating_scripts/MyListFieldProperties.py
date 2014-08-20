#-------------------------------------------------------------------------------
# Name:        MyListFieldProperties.py
# Purpose:
#
# Author:      Jun Dang
#
# Created:     19/08/2014
# Copyright:   (c) Jun Dang 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy
wksp = "C:\Student\PYTH\Automating_scripts"
arcpy.env.workspace =os.path.join(wksp, "SanDiego.gdb")
field_list = arcpy.ListFields("MajorAttractions")
txtFile = open(os.path.join(wksp,"MajorAttractions.txt"), "w")
txtFile.write("MajorAttractions field information" + "\n")
txtFile.write("----------------------------------" + "\n")
for field in field_list:
    line = "Name: {}, Type: {}, Length: {}\n".format(field.name, field.type, field.length)
    txtFile.write(line)
txtFile.close()
print "Script completed"
