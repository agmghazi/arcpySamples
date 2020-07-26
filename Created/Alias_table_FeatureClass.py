import arcpy
from arcpy import env
import csv
import os

# Set workspace
# env.workspace = r"C:\Users\L\Downloads\Compressed\SHP for Arcpy"
arcpy.env.overwriteOutput = True    # this for re write new data in old data and replace it 


# Creating a spatial reference object

csvDataSets = r"D:\Applications\SHP for Arcpy\ArcPy Code\Created\Files/csvRenameFeatureClasss.csv"
# Set local variables
NamberOfRenameFeatreClasss = 0


# read data from csv file
csv.register_dialect("xls", delimiter=",", lineterminator="\n")
CSVcreateFeature = open(csvDataSets, "r")
dataSetReader = csv.reader(CSVcreateFeature, "xls")
for aliasFeature in dataSetReader:
    if aliasFeature[1] == aliasFeature[2]:
        out_dataset_path = r'D:\filetest\out\DWHGDB.gdb\Electercity' +'\\'+ aliasFeature[1]
        # arcpy.CreateTable_management('c:/city/Boston.gdb', 'SnowReport')
        arcpy.AlterAliasName(out_dataset_path, aliasFeature[0])
        NamberOfRenameFeatreClasss += 1
        print 'Alias: ' + aliasFeature[0]+" Feeature Classs: " +aliasFeature[1] 

print '----------------------------------'
print 'Finish Rename FeatureClasss' 
print "Result: {} Rename FeatureClasss" .format(NamberOfRenameFeatreClasss)
print '----------------------------------'


