import arcpy
import csv
import os
arcpy.env.overwriteOutput = True    # this for re write new data in old data and replace it 
arcpy.env.workspace = "D:\filetest\gdp\test.gdb"

csvFields = r"D:\filetest\csvFields.csv"
csvFeatures = r"D:\filetest\csvFeatures.csv"
csvDataSets = r"D:\filetest\csvDatasets.csv"
out_dataset_path = r"D:\filetest\out\AmanaGDB.gdb"
fileGDB_Name = "AmanaGDB.gdb"
current_version_GDB = "10.0"
fileGDB_path = r'D:\filetest\out'
spatialref = arcpy.Describe("C:\Users\L\Downloads\Compressed\SHP for Arcpy\Ports.shp").spatialReference
FeatureClass = r'D:\filetest\out\AmanaGDB.gdb\\'     #loop this feature class
total_count = 0
created_Point_count = 0
created_Polygon_count = 0
created_Polyline_count = 0
created_Fildes_count = 0
baseRow = []
secondRow = []

# create Files Geo database 
arcpy.CreateFileGDB_management(fileGDB_path,fileGDB_Name ,current_version_GDB)
print 'Successfully create FileGDB :'+ fileGDB_Name

# create feature class
csv.register_dialect("xls", delimiter=",", lineterminator="\n")
CSVcreateFeature = open(csvFeatures, "r")
reader = csv.reader(CSVcreateFeature, "xls")

# read data from csv file
csv.register_dialect("xls", delimiter=",", lineterminator="\n")
CSVcreateFeature = open(csvDataSets, "r")
reader = csv.reader(CSVcreateFeature, "xls")
for dataSetRow in reader:
# Execute CreateFeaturedataset 
 arcpy.CreateFeatureDataset_management(out_dataset_path, dataSetRow[0], spatialref)
 print 'Successfully create Dataset :' + dataSetRow[0]
 
# create feature class
for FeatureRow in reader:
    print FeatureRow[3]
    total_count +=1
    baseRow.append(FeatureRow[0])
    for x in baseRow:
      a= baseRow.__len__()
    print FeatureRow[3]
    if FeatureRow[1] == 'POINT':
      outName = FeatureRow[0]
      geometrytype ='POINT'
      created_Point_count +=1
      CreateFeatureClassParameters = {"out_path" : FeatureClass+dataSetRow[0],
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
      print "successfully create Point Features: " +FeatureRow[0]    
elif FeatureRow[1] == 'POLYGON':
     outName = FeatureRow[0]
     geometrytype = FeatureRow[1]
     created_Polygon_count +=1
     CreateFeatureClassParameters = {"out_path" : FeatureClass,
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
     print "successfully create POLYGON Features: " +FeatureRow[0]   
  else :
     outName = FeatureRow[0]
     geometrytype = FeatureRow[1]
     created_Polyline_count +=1
     CreateFeatureClassParameters = {"out_path" : FeatureClass,
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
     print "successfully create Polyline Features: " +FeatureRow[0]

# You can tweak these CreateFeatureclass_management parameters before calling the function.
CSVcreateFeature.close()
print 'Finish Created Features'
print "Result: {0} all created Features and {1} created Point Feature and {2} created Line Feature and {3} created Polygon Feature".format(total_count,created_Point_count,created_Polyline_count,created_Polygon_count)    

# Read the CSV table and store some header information in a dictionary.
csv.register_dialect("xls", delimiter=",", lineterminator="\n")
CSVcreateFiled = open(csvFields, "r")
reader = csv.reader(CSVcreateFiled, "xls")
header = reader.next()
headerdict = dict()
for index, value in enumerate(header):
    headerdict[value] = index
for getFiledsRows in reader:
 secondRow.append(getFiledsRows)
 for fieldRow in secondRow:
    # print 'successfully create field: '+ fieldRow[0]
    print ''
 for x in baseRow:
   if x == getFiledsRows[0]:
        # print  type(rows[2])
    for FeatureClassName in FeatureClass:
       FeatureClassName=FeatureClass +'\\'+dataSetRow[0]+'\\'+ getFiledsRows[0]     #here add feaure calss name
       AddFieldParameters = {"in_table" : FeatureClassName,
                          # "field_name" : row[headerdict["Field Name"]],
                          "field_name" : fieldRow[1],
                          "field_type" : fieldRow[2],
                          "field_precision" : None,
                          "field_scale" : None,
                          "field_length" : fieldRow[3],
                          "field_alias" : fieldRow[4],
                          "field_is_nullable" : "NULLABLE",
                          "field_is_required" : "NON_REQUIRED",
                          "field_domain" : None}
    # arcpy.AddField_management(**AddFieldParameters)
    created_Fildes_count +=1
CSVcreateFiled.close()
# print 'Finish Created Fileds'
# print "Result: {} created Fildes ".format(created_Fildes_count)