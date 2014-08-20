######################################################################
## UpdateMxd.py
## 
## Challenge script without pseudocode
######################################################################

# Challenge
import arcpy
## Step 1
import arcpy.mapping as MAP

## Challenge
import os, sys

# Challenge - Obtain directory location from input parameter
mxd_dir = arcpy.GetParameterAsText(0)

# Challenge - Check for valid directory/folder
if os.path.exists(mxd_dir) == False:
    sys.exit("1, Invalid path specified.  Re-run script with valid path.")

# Challenge - Set the current workspace for the list function    
arcpy.env.workspace = mxd_dir

# Challenge - Obtain list of mxds in the current folder
mxd_list = arcpy.ListFiles("*.mxd")

# Challenge - Loop through list, join path and mxd name
# Process mxd
for name in mxd_list:
    mxdFile = os.path.join(mxd_dir, name)
    mxd = MAP.MapDocument(mxdFile)
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
    elemList = MAP.ListLayoutElements(mxd, "TEXT_ELEMENT")
    mxd.title = "Corvallis Meters map"

    for elem in elemList:
        if elem.name == "Corvallis Meters":
            elem.text = "Central Park Meters"

    mxd_copy = name[:-4] + "_updated.mxd"
    mxd.saveACopy(os.path.join(mxd_dir, mxd_copy))
    del mxd
