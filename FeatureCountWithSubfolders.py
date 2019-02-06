import os
import arcpy

directory = r"X:\Projects_2017\Corelogic Parcel\Supplementary Data Attributes\pyTest"
for root, dirs, files2 in os.walk(directory):
    for dir in dirs:
            for root, dirs, files in os.walk(directory + "/" + dir):
                ct = 0
                for file in files:
                    if file.endswith(".shp"):
                        pth = os.path.join(directory + "/" + dir,file)
                        filename = file.replace(".shp","")
                        arcpy.MakeFeatureLayer_management(pth,filename)
                        result = arcpy.GetCount_management(file)
                        count = int(result.getOutput(0))
                        ct += count
            print(ct)
