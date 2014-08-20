######################################################################
## ChallengeScript.py
## 
## 
######################################################################

import arcpy

# Optional step:
arcpy.env.workspace = "C:/Student/PYTH/Describing_data/Tahoe/All"

# Optional step:
desc = arcpy.Describe("C:/Student/PYTH/Describing_data/Tahoe/Emer/erelev")
rasExtent = desc.extent
print rasExtent
print desc.spatialReference.name
