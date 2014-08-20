import arcpy

flds = "ESTAB; ADDR; EMP; NAME"

newFld = "STATE_NAME"
in_table = "C:/Student/PYTH/Exercise06/SanDiego.gdb/MajorAttractions"
field_name = "STATE_NAME"

arcpy.AddField_management (in_table, field_name, "TEXT")

cur = arcpy.da.UpdateCursor(in_table, field_name)

for row in cur:
    row[0] = "CALIFORNIA"
    cur.updateRow(row)

del cur