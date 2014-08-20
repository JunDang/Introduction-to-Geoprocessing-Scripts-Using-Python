#-------------------------------------------------------------------------------
# Name:        MyParcel_Acres.py
# Purpose:
#
# Author:      Jun Dang
#
# Created:     20/08/2014
# Copyright:   (c) Jun Dang 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#question6 AddField_management (in_table, field_name, field_type, {field_precision}, {field_scale}, {field_length}, {field_alias}, {field_is_nullable}, {field_is_required}, {field_domain})
import arcpy
arcpy.env.workspace = "C:/Student/PYTH/Cursors/Corvallis.gdb"
#arcpy.AddField_management ("Parcel", "ACRES", "DOUBLE")
#UpdateCursor (in_table, field_names, {where_clause}, {spatial_reference}, {explode_to_points}, {sql_clause})
with arcpy.da.UpdateCursor("Parcel", ["ACRES","SHAPE@AREA"]) as Cursor:
    for row in Cursor:
        row[0] = row[1] / 43560
        Cursor.updateRow(row)
