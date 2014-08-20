##------------------------------------------------------------------------------
## Name:        UpdateGraduatedColorsSymbology.py
## Purpose:
##
## Author:      Wsri
##
## Created:     Jun 11, 2013
## Copyright:   (c) Esri 2013
##------------------------------------------------------------------------------
import arcpy
mxd = arcpy.mapping.MapDocument(r"C:\student\PYTH\SampleData\MyProject.mxd")
df = arcpy.mapping.ListDataFrames(mxd, "Census")[0]
lyr = arcpy.mapping.ListLayers(mxd, "StatePopulation", df)[0]
lyrFile = arcpy.mapping.Layer(r"C:\Student\PYTH\SampleData\Population.lyr")
arcpy.mapping.UpdateLayer(df, lyr, lyrFile, True)
if lyr.symbologyType == "GRADUATED_COLORS":
  lyr.symbology.valueField = "POP2000"
  lyr.symbology.classBreakValues = [250000, 999999, 4999999, 9999999, 35000000]
  lyr.symbology.classBreakLabels = ["250,000 to 999,999", "1,000,000 to 4,999,999",
                                    "5,000,000 to 9,999,999", "10,000,000 to 35,000,000"]
#arcpy.mapping.ExportToPDF(mxd, r"C:\student\PYTH\SampleData\StatePopulation.pdf")
del mxd, lyrFile
