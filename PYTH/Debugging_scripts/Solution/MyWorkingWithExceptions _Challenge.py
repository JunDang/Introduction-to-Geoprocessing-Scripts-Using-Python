######################################################################
## WorkingWithExceptions.py
## Purpose:  Work with different exception handlers in a try-except
##
######################################################################

import arcpy
import sys
import traceback

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

try:
    # Variable assignments for GP tasks
    fc1 = "MajorAttractions"
    fc2 = "Railroads"
    fc1Lyr = "MjrAttractLyr"
    fc2Lyr = "RailLyr"
    fc3 = "ClipAttractions"
    fields = ["NAME", "ADDR", "CITYNM", "ZIP"]
    SQLExp = """ "STREET_NAM" LIKE '%TROLLEY' """

    # Create Feature Layers
    arcpy.MakeFeatureLayer_management(fc1, fc1Lyr)
    arcpy.MakeFeatureLayer_management(fc2, fc2Lyr, SQLExp)

    # Perform spatial selection
    arcpy.SelectLayerByLocation_management(fc1Lyr, "WITHIN_A_DISTANCE",
                                           fc2Lyr, "2640 feet", "NEW_SELECTION")

    # Loop through selected features
    print "MajorAttractions within 0.5 mile of Trollies\n"
    with arcpy.da.SearchCursor(fc1Lyr, fields) as cursor:
       for row in cursor:
           print "{0}\n{1}\n{2}, CA {3}\n".format(row[0],row[1], row[2],row[3])

    arcpy.CopyFeatures_management(fc1Lyr, fc3)

    # Remove feature layers from memory
    arcpy.Delete_management(fc1Lyr)
    arcpy.Delete_management(fc2Lyr)

##except:
##    print "An error occurred"
##    print arcpy.GetMessages()
##except Exception as e:
##    print e
except arcpy.ExecuteError:
    print "A geoprocessing error has occurred"
    print arcpy.GetMessages(2)
except:
        # Return any Python specific errors and any error returned by the geoprocessor
        #
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n    " + \
                str(sys.exc_type)+ ": " + str(sys.exc_value) + "\n"
        arcpy.AddError(pymsg)

        msgs = "GP ERRORS:\n" + arcpy.GetMessages(2) + "\n"
        arcpy.AddError(msgs)
        print pymsg + "\n"
        print msgs

print "Script completed"