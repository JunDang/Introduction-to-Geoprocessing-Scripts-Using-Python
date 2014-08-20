##------------------------------------------------------------------------------
## Name:        MyListFieldProperties.py
## Purpose:     Creates a list of fields from a feature class and writes
##              the field properties to a new text file.
##
## Author:      Student
##
## Created:     May 23, 2013
## Copyright:   (c) Esri Student 2013
##------------------------------------------------------------------------------

import arcpy
import os
wksp = "C:/Student/PYTH/Automating_scripts"
arcpy.env.workspace = os.path.join(wksp, "SanDiego.gdb")

field_list = arcpy.ListFields("MajorAttractions")

txtFile = open(os.path.join(wksp, "MajorAttractions.txt"), "w")
txtFile.write("MajorAttractions field information" + "\n")
txtFile.write("-------------------------------------" + "\n")
for field in field_list:
    line = "Name: {}, Type: {}, Length: {}\n".format(
         field.name, field.type, field.length)
    txtFile.write(line)

txtFile.close()
print "Script completed"
