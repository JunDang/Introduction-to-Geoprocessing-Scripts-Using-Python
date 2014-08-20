######################################################################
## UpdateLogoInLayout.py
## 
## Replaces logo placeholder in layout with specified logo
######################################################################

import arcpy

mxDoc = "C:/Student/PYTH/CityBase.mxd"
# Replace City logo placeholder in template with bmp
# mxDoc points to map document object
for picElem in arcpy.mapping.ListLayoutElements(
                  mxDoc, "PICTURE_ELEMENT")
     if picElem.name == "CityLogo":
          picElem.sourceImage = "C:\Images\BryceCanyon.bmp"
mxd.saveACopy(r"C:\Project1\Bryce Map.mxd")
