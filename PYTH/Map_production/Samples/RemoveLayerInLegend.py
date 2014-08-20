######################################################################
## RemoveLayerInLegend.py
## 
## Removes layer from legend in current map document
######################################################################

import arcpy

# Remove layer in legend to make room for other layers
mxd = arcpy.mapping.MapDocument("CURRENT")
legendElem = arcpy.mapping.ListLayoutElements(mxd, "LEGEND_ELEM")[0]
if legendElem.isOverFlowing:
     removeLyr = arcpy.mapping.ListLayers(mxd, "StateBnd")[0]
     legendElem.removeItem(removeLyr)
mxd.save()
arcpy.RefreshActiveView()
