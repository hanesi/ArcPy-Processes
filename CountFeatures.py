import os
import arcpy

directory = r"C:\Users\hanesi\Desktop\Projects\Python\10"
for root, dirs, files in os.walk(directory):
    ct = 0
    for file in files:
        if file.endswith(".shp"):
            pth = os.path.join(directory,file)
            filename = file.replace(".shp","")
            arcpy.MakeFeatureLayer_management(pth,filename)
            result = arcpy.GetCount_management(file)
            count = int(result.getOutput(0))
            ct += count
print(ct)
