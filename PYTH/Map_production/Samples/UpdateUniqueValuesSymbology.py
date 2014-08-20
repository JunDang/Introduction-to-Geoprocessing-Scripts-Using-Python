##------------------------------------------------------------------------------
## Name:        UpdateUniqueValuesSymbology.py
## Purpose:
##
## Author:      Esri
##
## Created:     Jun 11, 2013
## Copyright:   (c) Esri 2013
##------------------------------------------------------------------------------
import arcpy
mxd = arcpy.mapping.MapDocument("CURRENT")
lyr = arcpy.mapping.ListLayers(mxd, "ParkingMeters")[0]
if lyr.symbologyType == "UNIQUE_VALUES":
  lyr.symbology.valueField = "TYPE"
  lyr.symbology.addAllValues()
arcpy.RefreshActiveView()
arcpy.RefreshTOC()
mxd.save()
del mxd
