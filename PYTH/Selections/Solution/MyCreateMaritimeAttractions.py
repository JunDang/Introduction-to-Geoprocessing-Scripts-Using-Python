##------------------------------------------------------------------------------
## Name:        MyCreateMaritimeAttractions.py
## Purpose:     Create new Maritime climate and Historic Attractions layer
##              Determine the historic attractions within the maritime climate
##              and copy the results to a new feature class
## Author:      Student
##
## Created:     May 24, 2013
## Copyright:   (c) Esri Student 2013
##------------------------------------------------------------------------------

import arcpy
arcpy.env.workspace = "C:/Student/PYTH/Selections/SanDiego.gdb"

newField1 = arcpy.AddFieldDelimiters(arcpy.env.workspace,"TYPE")
newField2 = arcpy.AddFieldDelimiters(arcpy.env.workspace,"ESTAB")
# TYPE = 'Maritime'
maritimeSQLExp = newField1 + " = " + "'Maritime'"
historicSQLExp = newField2 + " > 0 and " + newField2 + " < 1956"

arcpy.MakeFeatureLayer_management("Climate", "MaritimeLyr", maritimeSQLExp)
arcpy.MakeFeatureLayer_management("MajorAttractions", "HistoricLyr",
                                    historicSQLExp)

arcpy.SelectLayerByLocation_management("HistoricLyr", "COMPLETELY_WITHIN",
                                        "MaritimeLyr", "", "NEW_SELECTION")

featCount = arcpy.GetCount_management("HistoricLyr")
print "Number of historic features selected: {}".format(featCount)
