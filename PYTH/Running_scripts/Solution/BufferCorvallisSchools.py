import arcpy
arcpy.env.workspace = "C:/Student/PYTH/Running_scripts/Corvallis.gdb"
arcpy.env.overwriteOutput = True
arcpy.Buffer_analysis("Schools", "BuffSchools1000", "1000 feet")
print "Script completed"
