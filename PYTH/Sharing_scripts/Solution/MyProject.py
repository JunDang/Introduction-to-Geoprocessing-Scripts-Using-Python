######################################################################
## MyProject.py
## Purpose:  Script a project workflow
##           Additional comments added to detail pseudocode
######################################################################

# Layers needed for fund raising event - Parks, Parking Meters
#  Streets, Building
# Need Parking meters within specified distance of Central Park

# Import arcpy module and set the current workspace
# Set the overwriteOutput environment setting to True
import arcpy
arcpy.env.workspace = "C:/Student/PYTH/Sharing_scripts/Corvallis.gdb"
arcpy.env.overwriteOutput = True

### Obtain script parameter values
distance = arcpy.GetParameterAsText(0)
output_FC = arcpy.GetParameterAsText(1)

SQLExp = """ "PARK_NAME" = 'Central Park' """

### Create Feature Layers
# Create Parks feature layer for Central Park
arcpy.MakeFeatureLayer_management("Parks", "CentralPark", SQLExp)

# Create Parking Meters feature layer for selection
arcpy.MakeFeatureLayer_management("ParkingMeters", "Meters")

### Perform spatial selection
# Select all Meters that are within specified distance of Central Park
arcpy.SelectLayerByLocation_management("Meters", "WITHIN_A_DISTANCE",
                                       "CentralPark", distance,
                                       "NEW_SELECTION")
### Update Flag field
with arcpy.da.UpdateCursor("Meters", ["FLAG"]) as cursor:
    for row in cursor:
        row[0] = "Y"
        cursor.updateRow(row)

### Copy selected meters to new feature class
arcpy.CopyFeatures_management("Meters", output_FC)

### Report selected meter count
count = arcpy.GetCount_management(output_FC)
print "Number of meters to program: {0}".format(count)

print "Script completed"

