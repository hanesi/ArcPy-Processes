"""
This script counts the number of features in a single folder
containing multiple shapefiles
"""
import os
import arcpy

#Input the parent file path
directory = r"FILE PATH"
for root, dirs, files in os.walk(directory):
    ct = 0
    for file in files:
        if file.endswith(".shp"):
            #Set the path of each individual file
            pth = os.path.join(directory,file)
            #Retrieve the filename (no extension, a requirement of the function)
            filename = file.replace(".shp","")
            #Create an in memory copy of each file and count the number of features
            arcpy.MakeFeatureLayer_management(pth,filename)
            result = arcpy.GetCount_management(file)
            count = int(result.getOutput(0))
            ct += count
print(ct)
