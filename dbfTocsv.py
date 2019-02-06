import arcpy
import csv
import os

directory = r"C:\Users\hanesi\Desktop\Projects\Python\10"
outloc = r"C:\Users\hanesi\Desktop\Projects\Python\10\csv"
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".dbf"):
            pth = os.path.join(directory,file)
            outpth = os.path.join(outloc,file)
            filename = file.replace(".dbf","")
            outfile = outpth.replace(".dbf",".csv")
            arcpy.MakeFeatureLayer_management(pth, filename)
            #--first lets make a list of all of the fields in the table
            fields = arcpy.ListFields(pth)
            field_names = [field.name for field in fields]

            with open(outfile,'wb') as f:
                dw = csv.DictWriter(f,field_names)
                #--write all field names to the output file
                dw.writeheader()

                #--now we make the search cursor that will iterate through the rows of the table
                with arcpy.da.SearchCursor(pth,field_names) as cursor:
                    for row in cursor:
                        dw.writerow(dict(zip(field_names,row)))
