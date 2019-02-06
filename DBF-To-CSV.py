"""
This file reads dBASE (.dbf) files and writes them as 
.csv's. Due to programmatic restrictions with ArcGIS,
these files have to be written using a cursor that 
grabs and writes data. While not the most efficient, 
it is currently the only way
"""
import arcpy
import csv
import os

directory = r"File Path to dBASE files"
outloc = r"File Path for csv outputs"
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".dbf"):
            #Create full file extensions for each file and the subsequent output
            pth = os.path.join(directory,file)
            outpth = os.path.join(outloc,file)
            #Create filename without extension (neccessary for MakeFeatureLayer) and output filename
            filename = file.replace(".dbf","")
            outfile = outpth.replace(".dbf",".csv")
            arcpy.MakeFeatureLayer_management(pth, filename)
            #List all fields
            fields = arcpy.ListFields(pth)
            field_names = [field.name for field in fields]

            with open(outfile,'wb') as f:
                dw = csv.DictWriter(f,field_names)
                #Write field names to output file
                dw.writeheader()

                #Use the search cursor to write the data
                with arcpy.da.SearchCursor(pth,field_names) as cursor:
                    for row in cursor:
                        dw.writerow(dict(zip(field_names,row)))
