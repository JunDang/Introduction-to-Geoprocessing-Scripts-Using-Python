######################################################################
## UpdateCreateFeatures.py
## Purpose:  Update location of existing feature, create new feature
##
######################################################################

import arcpy
arcpy.env.workspace = r"C:\Student\PYTH\Geometry_objects\SanDiego.gdb"

# Variables
featClass = "MajorAttractions"
fields = ["SHAPE@XY"]
exp = """ "NAME" = 'BALBOA PARK' """

# Step 4 variables
featClass2 = "Freeways"
fields2 = ["SHAPE@", "STREET_NAM"]
fldVal = "Balboa Park Drive"

pnt = arcpy.Point()
pnt.X = 6285430.0
pnt.Y = 1844965.66

with arcpy.da.UpdateCursor(featClass, fields, exp) as cur:
    for row in cur:
        print row[0]
        row[0] = pnt
        cur.updateRow(row)

print "Update completed"

# Step 4 code
ary = arcpy.Array()
coords = [[6284696.620, 1844282.464], [6284739.145, 1844632.515],
          [6284919.091, 1844881.011], [6285184.726, 1845026.683],
          [6285423.068, 1845060.988]]
for coord in coords:
    pnt.X = coord[0]
    pnt.Y = coord[1]
    ary.add(pnt)

polyLine = arcpy.Polyline(ary)

cur2 = arcpy.da.InsertCursor(featClass2, fields2)
cur2.insertRow([polyLine, fldVal])
del cur2
