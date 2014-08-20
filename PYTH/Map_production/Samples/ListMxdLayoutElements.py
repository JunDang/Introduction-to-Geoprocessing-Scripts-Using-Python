######################################################################
## ListMxdLayoutElements.py
## 
## 
######################################################################

import arcpy

mxDoc = "C:/Student/PYTH/CityBase.mxd"
# List text element properties in the layout
txtElem = arcpy.mapping.ListLayoutElements(mxDoc, "TEXT_ELEMENT")
for elem in txtElem:
     print "Name: {0} text: {1}".format(
             elem.name, elem.text)
     