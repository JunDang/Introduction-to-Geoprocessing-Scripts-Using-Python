######################################################################
## ReportShapeGeometry.py
## Purpose: Report X,Y,ID,length of Freeways features
##
######################################################################

import arcpy
arcpy.env.workspace = r"C:\Student\PYTH\Geometry_objects\SanDiego.gdb"

for row in arcpy.da.SearchCursor("Freeways",
                                 ["SHAPE@XY", "OID@", "SHAPE@LENGTH"]):
    print "X: {0}, Y: {1}, ID: {2}, length: {3}".format(row[0][0],
                                                        row[0][1],
                                                        row[1], row[2])