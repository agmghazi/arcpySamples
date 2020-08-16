import arcpy
from arcpy import env
import csv
import os

arcpy.env.overwriteOutput = True    # this for re write new data in old data and replace it 
csvDomainToField = r'D:\Applications\SHP for Arcpy\ArcPy Code\Created\Files\AssignDomainToField.csv'
# Set the workspace (to avoid having to type in the full path to the data every time)
arcpy.env.workspace = r"D:\filetest\out"
# gdb = "DWHGDB.gdb"

   # read data from csv file
csv.register_dialect("xls", delimiter=",", lineterminator="\n")
csvDomainToField = open(csvDomainToField, "r")
readers = csv.reader(csvDomainToField, "xls")
for doaminRow in readers:
    inFeatures = "DWHGDB.gdb\RoadNetwork"    #Always change dataset name 
    inFeaturess = inFeatures +'\\'+ doaminRow[0]
# # Process: Constrain the material value of distribution mains
    arcpy.AssignDomainToField_management(inFeaturess, doaminRow[1], doaminRow[2])
    print 'create domain: {} in field: {} in Feature: {}'.format(doaminRow[2],doaminRow[1],doaminRow[0])