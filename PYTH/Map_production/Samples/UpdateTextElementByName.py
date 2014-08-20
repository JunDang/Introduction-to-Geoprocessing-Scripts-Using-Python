######################################################################
## UpdateTextElementByName.py
## 
## Locates text element by name and updates value
######################################################################

import arcpy

mxDoc = "C:/Student/PYTH/CityBase.mxd"
# Update text value in a text element
#  based on the element name.
# mxDoc points to map document object.
for txtElem in arcpy.mapping.ListLayoutElements(mxDoc, "TEXT_ELEMENT")
     if txtElem.name == "Revision Date":
          txtElem.text = "Revised on " + time.ctime()
mxd.saveACopy(r"C:\Student\PYTH\Map_production\Map1.mxd")
