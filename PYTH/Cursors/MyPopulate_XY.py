#-------------------------------------------------------------------------------
# Name:        MyPopulate_XY.py
# Purpose:
#
# Author:      Jun Dang
#
# Created:     20/08/2014
# Copyright:   (c) Jun Dang 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Import the arcpy module and set the current workspace
import arcpy
arcpy.env.workspace = "C:/Student/PYTH/Cursors/Corvallis.gdb"

rowValues = [["Benton", (-123.40, 44.49)], ["Linn", (-122.49, 44.48)],["Polk", (-123.38, 44.89)],["Tillamook", (-123.65, 45.45)]]
arcpy.CreateFeatureclass_management (arcpy.env.workspace, "CountyPNT", "POINT")
arcpy.AddField_management ("CountyPNT", "NAME", "TEXT")

iCur = arcpy.da.InsertCursor("CountyPNT", ["NAME", "SHAPE@XY"])

for row in rowValues:
    iCur.insertRow(row)

del iCur
print "Script completed"