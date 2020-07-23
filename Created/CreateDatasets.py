import arcpy
from arcpy import env
import csv
import os

# Set workspace
# env.workspace = r"C:\Users\L\Downloads\Compressed\SHP for Arcpy"
arcpy.env.overwriteOutput = True    # this for re write new data in old data and replace it 


# Creating a spatial reference object
spatialref = arcpy.SpatialReference("D:\Applications\SHP for Arcpy\Ports.prj")
# spatialref = arcpy.Describe("D:\Applications\SHP for Arcpy\Ports.shp").spatialReference

csvDataSets = r"D:\Applications\SHP for Arcpy\ArcPy Code\Created\Files\DataSetNames.csv"
# Set local variables
out_dataset_path = r"D:\filetest\out\DWHGDB.gdb" 
fileGDB_path = r'D:\filetest\out'
current_version_GDB = "10.0"
fileGDB_Name = "DWHGDB.gdb"
NamberOfDataSets = 0
# dataSet_Name = "NewDataSet"

arcpy.CreateFileGDB_management(fileGDB_path,fileGDB_Name ,current_version_GDB)
print 'Successfully create FileGDB :' + fileGDB_Name

# read data from csv file
csv.register_dialect("xls", delimiter=",", lineterminator="\n")
CSVcreateFeature = open(csvDataSets, "r")
dataSetReader = csv.reader(CSVcreateFeature, "xls")
for dataSet in dataSetReader:
  # Execute CreateFeaturedataset 
 arcpy.CreateFeatureDataset_management(out_dataset_path, dataSet[0], spatialref)
 NamberOfDataSets += 1
 print 'Create Dataset : ' + dataSet[0]

print '----------------------------------'
print 'Finish Created Datasets' 
print "Result: {} Create Datasets" .format(NamberOfDataSets)
print '----------------------------------'
