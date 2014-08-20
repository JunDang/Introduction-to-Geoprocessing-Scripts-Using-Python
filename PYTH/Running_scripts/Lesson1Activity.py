######################################################################
## Lesson1Activity.py
## Purpose:  Demonstrate functionality in the arcpy module and automation
##           of tasks.  Also demonstrate ArcPy data access functionality
## 
######################################################################

# Import the arcpy module and set the workspace environment
import arcpy
import os
arcpy.env.workspace = r'C:\Student\PYTH\Running_scripts\Wilson.gdb'

# The ArcPy site package contains functions to list data
# This step will list all of the feature classes in the 
#  Wilson geodatabase
#
# Create a list of feature classes in the current workspace
fc_list = arcpy.ListFeatureClasses()
# Using the Python os.path basename function,
#  print the name of the geodatabase
print "Feature classes in: " + os.path.basename(arcpy.env.workspace)
# Loop through the list of feature classes and print the name
for name in fc_list:
    print name

# Your scripts can also access geoprocessing tools functionality
# Using the same list of feature classes, print the name and the
#  number of features.
# Print the results using the Python str.format() function
print "Feature counts"
for name in fc_list:
    count = arcpy.GetCount_management(name)
    print "Name: {0}, feature count: {1}".format(name, count)

# Your scripts can also access and work with values in feature classes
#  and tables, using the arcpy.da cursors.
# The script will work with the SearchCursor to access field values in
#  a feature class.
print "Feature attribute values"
with arcpy.da.SearchCursor("Wilson_Schools", "NAME") as cursor:
    for row in cursor:
        print "School Name: " + row[0]

print "Script completed"
