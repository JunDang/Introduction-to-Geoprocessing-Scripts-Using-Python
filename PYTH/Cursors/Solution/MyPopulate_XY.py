######################################################################
## Populate_XY.py
## Purpose:  Work with an arcpy.da InsertCursor to populate new features
## 
######################################################################

# Import the arcpy module and set the current workspace
import arcpy
arcpy.env.workspace = "C:/Student/PYTH/Cursors/Corvallis.gdb"

# Create a list of name and coordinate pairs.
rowValues = [["Benton", (-123.40, 44.49)], ["Linn", (-122.49, 44.48)],
             ["Polk", (-123.38, 44.89)], ["Tillamook", (-123.65, 45.45)]]

# Create a new Point feature class and name it CountyPNT
arcpy.CreateFeatureclass_management(arcpy.env.workspace, "CountyPNT", "Point")

# Add the Name field to CountyPNT
arcpy.AddField_management("CountyPNT", "NAME", "TEXT")

# Create an arcpy.da.InsertCursor on CountyPNT
iCur = arcpy.da.InsertCursor("CountyPNT", ["NAME", "SHAPE@XY"])

for row in rowValues:
    iCur.insertRow(row)

# Delete the cursor to close the cursor and release the exclusive lock
del iCur

print "Script completed"
