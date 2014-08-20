######################################################################
## Name: CreateFeatureLayerWithFieldInfo.py
## Purpose:  Demostrate how to use a FieldInfo object with the
##           MakeFeatureLayer tool to create a feature layer
##           containing an altered field name
######################################################################

# Import the ArcPy site package and set the current workspace
import arcpy
arcpy.env.workspace = "C:/Student/PYTH/Selections/Corvallis.gdb"

# Variables
fldName = "PARK_NAME"
newFldName = "NAME"

# Create the FieldInfo object
fldInfo = arcpy.FieldInfo()

# The PARK_NAME field is to be changed to NAME in the feature layer
# Add the change to the FieldInfo object
fldInfo.addField(fldName, newFldName, "VISIBLE", "")

# Set up SQL expression for MakeFeatureLayer where_clause parameter
# We will want a subset of parks features that are large area parks
# in the new feature layer.
featureClass = "Parks"
featLayer = "ParksLyr"
newFeatureClass = "LargeParks"
fieldName = "Shape_area"

# Where clause:  ESTAB > 0 and ESTAB < 1956
SQLExp = fieldName + " > 200000"

# Apply SQL expression and FieldInfo object to the MakeFeatureLayer tool
arcpy.MakeFeatureLayer_management(featureClass, featLayer, SQLExp,
                                  "", fldInfo)

# Create a new feature class form the feature layer.
# The new feature class will contain only large area parks.
arcpy.CopyFeatures_management(featLayer, newFeatureClass)

print "Script completed"
