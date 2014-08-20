#-------------------------------------------------------------------------------
# Name:        MyCreateMaritimeAttractions.py
# Purpose:
#
# Author:      Jun Dang
#
# Created:     20/08/2014
# Copyright:   (c) Jun Dang 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy
arcpy.env.workspace = "C:\Student\PYTH\Selections\SanDiego.gdb"
arcpy.env.overwriteOutput = True
newField1 = arcpy.AddFieldDelimiters(arcpy.env.workspace, "TYPE")
newField2 = arcpy.AddFieldDelimiters(arcpy.env.workspace, "ESTAB")
maritimeSQLExp = newField1 + " = " + " 'Maritime'"  # TYPE = 'Maritime'
historicSQLExp = newField2 + " > 0 and " + newField2 + " < 1956"
#arcpy.Delete_management("MaritimeLyr1")
arcpy.MakeFeatureLayer_management ("Climate", "MaritimeLyr", maritimeSQLExp)
arcpy.MakeFeatureLayer_management ("MajorAttractions", "HistoricLyr", historicSQLExp)
arcpy.SelectLayerByLocation_management("HistoricLyr", "COMPLETELY_WITHIN", "MaritimeLyr","", "NEW_SELECTION")
featCount = arcpy.GetCount_management("HistoricLyr")
print featCount
arcpy.CopyFeatures_management("HistoricLyr", "MaritimeAttractions")
arcpy.Delete_management("HistoricLyr")
arcpy.Delete_management("MaritimeLyr")
print "Script completed"

