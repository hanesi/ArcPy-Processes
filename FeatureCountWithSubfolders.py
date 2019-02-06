"""
This script counts the number of features in a shape files
with multiple subfolders. It returns the parent folder and
the number of features.
"""
import os
import arcpy

directory = r"FILE PATH"
#Set parent directory
for root, dirs, files2 in os.walk(directory):
    #Walk through sub folders in parent directory
    for dir in dirs:
            for root, dirs, files in os.walk(directory + "/" + dir):
                ct = 0
                for file in files:
                    if file.endswith(".shp"):
                        #Construct file path
                        pth = os.path.join(directory + "/" + dir,file)
                        #Retrieve file name (no extension, a requirement of the function)
                        filename = file.replace(".shp","")
                        #Create in memory copy of file and count the features
                        arcpy.MakeFeatureLayer_management(pth,filename)
                        result = arcpy.GetCount_management(file)
                        count = int(result.getOutput(0))
                        ct += count
            print(dir + ": " + str(ct))
            
