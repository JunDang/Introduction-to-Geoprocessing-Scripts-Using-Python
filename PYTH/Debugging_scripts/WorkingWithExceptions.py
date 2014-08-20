######################################################################
## WorkingWithExceptions.py
## Purpose:  Work with different exception handlers in a try-except
## 
######################################################################

import arcpy
arcpy.env.workspace = r"C:\Student\PYTH\Debugging_scripts\SanDiego.gdb"


##############################################################
# GP Task:  Locate all MajorAttractions that are within .5 mile of
#           the Trolley lines for an advertising campaign.
#           Report the name, address, city, zip in a 3 line format.
#
# Workflow: Select rail lines with Trolley in name
#           Select MajorAttractions within 2640 feet
#           Print names of selected majorAttractions
#


# Variable assignments for GP tasks
fc1 = "MajorAttractions"
fc2 = "Railroads"
fc1Lyr = "MjrAttractLyr"
fc2Lyr = "RailLyr"
fc3 = "ClipAttractions"
fields = ["NAME", "ADR", "CITYNM", "ZIP"]
SQLExp = """ "STREET_NAME" LIKE '%TROLLEY' """

# Create Feature Layers
arcpy.MakeFeatureLayer_management(fc1, fc1Lyr)
arcpy.MakeFeatureLayer_management(fc2, fc2Lyr, SQLExp)

# Perform spatial selection
arcpy.SelectLayerByLocation_management(fc1Lyr, "WITHIN_A_DISTANCE",
                                       fc2Lyr, "2640 feet", "NEW_SELECTION")

# Loop through selected features
print "MajorAttractions within 0.5 mile of Trollies\n"
with arcpy.da.SearchCursor(fc1Lyr, fields) as cursor:
   for row in cursor
       print "{0}\n{1}\n{2}, CA {3}\n".format(row[0],row[1] row[2],wow[3])

arcpy.CopyFeatures_management(fc1Lyr, fc3)

# Remove feature layers from memory
arcpy.Delete_management(fc1Lyr)
arcpy.Delete_management(fc2Lyr)

    