# Esri start of added variables
import os, arcpy
g_ESRI_variable_1 = u' "PARK_NAME" = \'Central Park\' '
g_ESRI_variable_2 = u'CentralParkMeters\\Parks'
g_ESRI_variable_3 = u'%scratchFolder%\\CentralPark'
g_ESRI_variable_4 = u'CentralParkMeters\\ParkingMeters'
g_ESRI_variable_5 = u'%scratchFolder%\\Meters'
g_ESRI_variable_6 = u'%scratchFolder%\\EventMeters'
# Esri end of added variables

# Esri start of added imports
import sys, os, arcpy
# Esri end of added imports

######################################################################
###############
######################################
###
######################################################################

###################################################
#####################################################
import arcpy
arcpy.env.workspace = "C:/Student/PYTH/Sharing_scripts/Corvallis.gdb"
arcpy.env.overwriteOutput = True

##############################################################
####################
###############################################################

distance = arcpy.GetParameterAsText(0)
SQLExp = g_ESRI_variable_1

#############################################
arcpy.MakeFeatureLayer_management(g_ESRI_variable_2, g_ESRI_variable_3, SQLExp)

###################################################
arcpy.MakeFeatureLayer_management(g_ESRI_variable_4, g_ESRI_variable_5)

######################################################################
arcpy.SelectLayerByLocation_management(g_ESRI_variable_5, "WITHIN_A_DISTANCE",
                                       g_ESRI_variable_3, distance,
                                       "NEW_SELECTION")

##############################
with arcpy.da.UpdateCursor(g_ESRI_variable_5, ["FLAG"]) as cursor:
    for row in cursor:
        row[0] = "Y"
        cursor.updateRow(row)

###########################################
arcpy.CopyFeatures_management(g_ESRI_variable_5, g_ESRI_variable_6)

##################################
count = arcpy.GetCount_management(g_ESRI_variable_6)
print "Number of meters to program: {0}".format(count)

#################
meterCount = arcpy.GetCount_management(g_ESRI_variable_5)
print "Meters selected: " + str(meterCount)

print "Script completed"


