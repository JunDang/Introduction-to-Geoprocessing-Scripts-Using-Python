######################################################################
## UpdateAllTextElements.py
## 
## Updates all text elements containing the same value with a new value
######################################################################

import arcpy

mxDoc = "C:/Student/PYTH/CityBase.mxd"
# Update text strings in all matching text elements
#   with the same text value.
# mxDoc points to map document object.
for txtElem in arcpy.mapping.ListLayoutElements(mxDoc, "TEXT_ELEMENT")
     if txtElem.text == "Replace Me":
          txtElem.text = "New value"
mxd.saveACopy(r"C:\Student\PYTH\Map_production\Map1.mxd")
