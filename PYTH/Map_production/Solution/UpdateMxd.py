######################################################################
## UpdateMxd.py
##
## results script without pseudocode
######################################################################

## Step 1
import arcpy.mapping as MAP

mxd = MAP.MapDocument(r"C:\Student\PYTH\Map_production\CorvallisMeters.mxd")
df = MAP.ListDataFrames(mxd)[0]

## Step 2
updateLayer = MAP.ListLayers(df, "ParkingMeters")[0]
sourceLayer = MAP.Layer(r"C:\Student\PYTH\Map_production\ParkingMeters.lyr")
MAP.UpdateLayer(df, updateLayer, sourceLayer, True)

addLayer = MAP.Layer(r"C:\Student\PYTH\Map_production\Schools.lyr")
MAP.AddLayer(df, addLayer)

refLayer = MAP.ListLayers(df, "Schools")[0]

## This is the tricky step.  The order of the arguments appears to be backwards.
MAP.MoveLayer(df, refLayer, updateLayer, "BEFORE")

## Step 3
mxd.title = "Corvallis Meters Map"
elemList = MAP.ListLayoutElements(mxd, "TEXT_ELEMENT")

for elem in elemList:
    if elem.name == "Corvallis Meters":
        elem.text = "Corvallis Parking Meters Inventory Report"

#mxd.saveACopy(r"C:\Student\PYTH\Map_production\CorvallisMeters_ks.mxd")
del mxd
