import arcpy
import csv
import os

arcpy.env.overwriteOutput = True    # this for re write new data in old data and replace it 
arcpy.env.workspace = "D:\filetest\gdp\test.gdb"
csvFields =r"D:\Applications\SHP for Arcpy\ArcPy Code\Created\Files\csvFields.csv"
csvFeatures = r"D:\Applications\SHP for Arcpy\ArcPy Code\Created\Files\csvFeatures.csv"
spatialref = arcpy.Describe("D:\Applications\SHP for Arcpy\Ports.shp").spatialReference
featureClassPath = r'D:\filetest\out\DWHGDB.gdb\Ports'  # "cane use this to create anything like shapefiles and feature class without datasets" featureClassPath = r'D:\filetest\out'
total_count = 0
created_Point_count = 0
created_Polygon_count = 0
created_Polyline_count = 0
created_fields_count = 0
featureBaseRow = []
FieldsSecondRow = []

# arcpy.SetProgressor("default", "Starting script...")

# Read the CSV table and store some header information in a dictionary.
# arcpy.SetProgressorLabel("Reading CSV Table")

csv.register_dialect("xls", delimiter=",", lineterminator="\n")
CSVcreateFeature = open(csvFeatures, "r")
createFeatureReader = csv.reader(CSVcreateFeature, "xls")
# header = createFeatureReader.next()
# headerdict = dict()
# for index, value in enumerate(header):
#     headerdict[value] = index

# Create a field for each row in the CSV, based on the header information obtained earlier.
for createFeatureRow in createFeatureReader:
    # print createFeatureRow[0]
    total_count +=1
    # print createFeatureRow[0]
    featureBaseRow.append(createFeatureRow[0])

    for x in featureBaseRow:
    #   print 'Get'+x
      a= featureBaseRow.__len__()
    #   print 'featureBaseRow: '+ str(a) 

    if createFeatureRow[1] == 'POINT':
     outName = createFeatureRow[0]
     geometrytype = createFeatureRow[1]
     created_Point_count +=1
     
     CreateFeatureClassParameters = {"out_path" : featureClassPath,
                                "out_name" : outName,
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
     print "successfully create Point Feature: " + createFeatureRow[0]  
    elif createFeatureRow[1] == 'POLYGON':
     outName = createFeatureRow[0]
     geometrytype = createFeatureRow[1]
     created_Polygon_count +=1
     CreateFeatureClassParameters = {"out_path" : featureClassPath,
                                "out_name" : outName,
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
     print "successfully create POLYGON Feature: " + createFeatureRow[0]   
    else :
     outName = createFeatureRow[0]
     geometrytype = createFeatureRow[1]
     created_Polyline_count +=1
     CreateFeatureClassParameters = {"out_path" : featureClassPath,
                                "out_name" : outName,
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
     print "successfully create Polyline Feature: " + createFeatureRow[0]

# Create the feature class.
# arcpy.SetProgressorLabel("Creating feature class")
# You can tweak these CreateFeatureclass_management parameters before calling the function.
CSVcreateFeature.close()
print '----------------------------------'
print 'Finish Created Features'
print "Result: {0} all created Features and {1} created Point Feature and {2} created Line Feature and {3} created Polygon Feature".format(total_count,created_Point_count,created_Polyline_count,created_Polygon_count)    
print '----------------------------------'

# Read the CSV table and store some header information in a dictionary.
# arcpy.SetProgressorLabel("Reading CSV Table")
csv.register_dialect("xls", delimiter=",", lineterminator="\n")
Csvcreatefields = open(csvFields, "r")
createFieldsReader = csv.reader(Csvcreatefields, "xls")
# header = reader.next()
# headerdict = dict()
# for index, value in enumerate(header):
#     headerdict[value] = index
for createFieldsRow in createFieldsReader:
 FieldsSecondRow.append(createFieldsRow)
 for fieldsAttributeRow in FieldsSecondRow:
    print 'successfully create field: {} ::FOR:: feature: {} '.format(fieldsAttributeRow[2],fieldsAttributeRow[0])
 for x in featureBaseRow:
   if x == createFieldsRow[0]:
        # print  type(createFieldsRow[2])
    for featureClassPathName in featureClassPath:
       featureClassPathName = featureClassPath +'\\'+ createFieldsRow[0]
       AddFieldParameters = {"in_table" : featureClassPathName,
                          # "field_name" : row[headerdict["Field Name"]],
                          "field_name" : fieldsAttributeRow[2],
                          "field_type" : fieldsAttributeRow[3],
                          "field_precision" : None,
                          "field_scale" : None,
                          "field_length" : fieldsAttributeRow[4],
                          "field_alias" : fieldsAttributeRow[5],
                          "field_is_nullable" : "NULLABLE",
                          "field_is_required" : "NON_REQUIRED",
                          "field_domain" : None}
    arcpy.AddField_management(**AddFieldParameters)
    created_fields_count +=1
Csvcreatefields.close()
# arcpy.ResetProgressor()
print '----------------------------------'
print 'Finish Created fields' 
print "Result: {} create fields ".format(created_fields_count)
print '----------------------------------'