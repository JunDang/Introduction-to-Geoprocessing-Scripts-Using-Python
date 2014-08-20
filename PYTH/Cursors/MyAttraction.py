#-------------------------------------------------------------------------------
# Name:        MyAttraction
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
arcpy.env.workspace = "C:/Student/PYTH/Cursors/SanDiego.gdb"

# Create a feature layer on MajorAttractions feature class
# Syntax: arcpy.MakeFeatureLayer_management (in_features, out_layer, {where_clause},
#                                           {workspace}, {field_info})
arcpy.MakeFeatureLayer_management("MajorAttractions", "AttractionsLyr")

# Syntax: arcpy.da.SearchCursor (in_table, field_names, {where_clause},
#                               {spatial_reference}, {explode_to_points}, {sql_clause})

with arcpy.da.SearchCursor("MajorAttractions", ["NAME", "ADDR", "CITYNM", "ZIP"]) as cursor:
    for row in cursor:
        print "{0}\n{1}\n{2}, CA {3}\n".format(row[0], row[1], row[2], row[3])
