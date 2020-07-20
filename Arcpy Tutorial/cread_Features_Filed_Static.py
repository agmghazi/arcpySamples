import arcpy
import csv
import os
arcpy.env.overwriteOutput = True    # this for re write new data in old data and replace it 


arcpy.SetProgressor("default", "Starting script...")


fc = r'D:\filetest\gdp\test.gdb\ab'
geometrytype = "POINT"
spatialref = arcpy.Describe("C:\Users\L\Downloads\Compressed\SHP for Arcpy\Ports.shp").spatialReference
csvtables = r"D:\filetest\TE.csv"

# Create the feature class.
arcpy.SetProgressorLabel("Creating feature class")
# You can tweak these CreateFeatureclass_management parameters before calling the function.
CreateFeatureClassParameters = {"out_path" : os.path.dirname(fc),
                                "out_name" : os.path.basename(fc),
                                "geometry_type" : geometrytype,
                                "template" : None,
                                "has_m" : "DISABLED",
                                "has_z" : "DISABLED",
                                "spatial_reference" : spatialref,
                                "config_keyword" : None,
                                "spatial_grid_1" : None,
                                "spatial_grid_2" : None,
                                "spatial_grid_3" : None}

arcpy.CreateFeatureclass_management(**CreateFeatureClassParameters)

# Read the CSV table and store some header information in a dictionary.
arcpy.SetProgressorLabel("Reading CSV Table")
csv.register_dialect("xls", delimiter=",", lineterminator="\n")
f = open(csvtables, "r")
reader = csv.reader(f, "xls")
header = reader.next()
headerdict = dict()
for index, value in enumerate(header):
    headerdict[value] = index

print 'Created Feature'

# Create a field for each row in the CSV, based on the header information obtained earlier.
for row in reader:
    print row[0]
    arcpy.SetProgressorLabel("Adding Field {0}".format(row[headerdict["Field Name"]]))
    # You can tweak these AddField_management parameters before calling the function.
    AddFieldParameters = {"in_table" : fc,
                          "field_name" : row[headerdict["Field Name"]],
                          "field_type" : row[headerdict["Field Type"]],
                          "field_precision" : None,
                          "field_scale" : None,
                          "field_length" : row[headerdict["Field Length"]],
                          "field_alias" : row[headerdict["Field Alias"]],
                          "field_is_nullable" : "NULLABLE",
                          "field_is_required" : "NON_REQUIRED",
                          "field_domain" : None}
    arcpy.AddField_management(**AddFieldParameters)

# Finish off the script.
f.close()
arcpy.ResetProgressor()

print 'Created Fileds'
