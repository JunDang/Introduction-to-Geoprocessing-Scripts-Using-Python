######################################################################
## CreateFeatureLayer.py
## Purpose: Create a feature layer on the MajorAttractions feature class
##          A SQL where clause will be applied to provide a subset of
##          features that have an establishment date prior to 1956
##
######################################################################

# Import the ArcPy site package and set the current workspace
import arcpy
arcpy.env.workspace = "C:/Student/PYTH/Selections/SanDiego.gdb"

# Variables
featureClass = "MajorAttractions"
featLayer = "SelMajorAttractions"
newFeatureClass = "HistoricAttractions"
fieldName = "ESTAB"
newFieldName = arcpy.AddFieldDelimiters(arcpy.env.workspace, fieldName)

# Where clause:  ESTAB > 0 and ESTAB < 1956
SQLExp = newFieldName + " > 0 and " + newFieldName + " < 1956"

# Create the feature layer, applying the where clause
arcpy.MakeFeatureLayer_management(featureClass, featLayer, SQLExp)

# Obtain the feature count for the feature layer
# Print feature count
featCount = arcpy.GetCount_management(featLayer)
print "Number of features in feature layer: {0}".format(featCount)

# Copy the feature layer to the permanent feature class
arcpy.CopyFeatures_management(featLayer, newFeatureClass)

print "Script Completed"