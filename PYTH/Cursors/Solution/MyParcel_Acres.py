######################################################################
## MyParcel_Acres.py
## Purpose:  Add new ACRES field to the Parcel feature class
##           and calculate the new field values
######################################################################

# Import the arcpy module and set the current workspace
import arcpy
arcpy.env.workspace = "C:/Student/PYTH/Cursors/Corvallis.gdb"

# Add a new field named ACRES to the Parcel feature class
#Syntax: arcpy.AddField_management (in_table, field_name, field_type, {field_precision},
#                                   {field_scale}, {field_length},
#                                   {field_alias}, {field_is_nullable},
#                                   {field_is_required}, {field_domain})
arcpy.AddField_management("Parcel", "ACRES", "Double")

# Update ACRES field.  Use SHAPE@ token and calculate acres
# The conversion from area in square feet to acres is:
# area value / 43560
# In the code below, a geometry object is returned from row[0]
# The area property is obtained from the SHAPE@AREA token, converted to acres
# and then assigned to the "ACRES" index position in the row list object.
with arcpy.da.UpdateCursor("Parcel", ["SHAPE@AREA", "ACRES"]) as cursor:
    for row in cursor:
        geom = row[0] # Obtain the shape geometry from the SHAPE@ token
        row[1] = geom / 43560 # Access the area value from the geometry shape and convert to acres
        cursor.updateRow(row)

print "Script completed"