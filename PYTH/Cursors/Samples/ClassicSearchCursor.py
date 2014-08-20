import arcpy

flds = "ESTAB; ADDR; EMP; NAME"

cur = arcpy.SearchCursor("C:/Student/PYTH/Exercise06/SanDiego.gdb/MajorAttractions",
                         "", "", flds)
for row in cur:
    print row.NAME, row.ESTAB, row.ADDR, row.EMP

del cur