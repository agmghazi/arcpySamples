import arcpy
from arcpy import env
import csv
import os

arcpy.env.overwriteOutput = True    # this for re write new data in old data and replace it 
csvDomain = r'D:\Applications\SHP for Arcpy\ArcPy Code\Created\Files\csvDomain.csv'
csvValueDomain = r'D:\Applications\SHP for Arcpy\ArcPy Code\Created\Files\csvValueDomain.csv'
# Set the workspace (to avoid having to type in the full path to the data every time)
arcpy.env.workspace = r"D:\filetest\out"
gdb = "DWHGDB.gdb"
valeDoaminRowArr =[]  
doaminRowArr =[]

csv.register_dialect("xls", delimiter=",", lineterminator="\n")
CSVvaleDoaminRow = open(csvValueDomain, "r")
reader = csv.reader(CSVvaleDoaminRow, "xls")
   # read data from csv file
csv.register_dialect("xls", delimiter=",", lineterminator="\n")
CSVcreateDomin = open(csvDomain, "r")
readers = csv.reader(CSVcreateDomin, "xls")
for doaminRow in readers:
    doaminRowArr.append(doaminRow[0])
    inFeatures = "DWHGDB.gdb\Setage\FC_Point"
    inField = "Name"
    print 'doaminRow[0]: '+ doaminRow[0]
    print 'doaminRow[1]: '+ doaminRow[1]
    arcpy.CreateDomain_management("DWHGDB.gdb", doaminRow[0], doaminRow[1], "TEXT", "CODED")   #Not allows type data (text) 
    print 'Finish create Domain Name: '+ doaminRow[0]
for valeDoaminRow in reader:
  for x in doaminRowArr:
        if  x == valeDoaminRow[0]:
            print 'valeDoaminRow: '+valeDoaminRow[0]
            print 'doaminRow: '+x
            arcpy.AddCodedValueToDomain_management(gdb, valeDoaminRow[0], valeDoaminRow[1], valeDoaminRow[2])
            print 'Finish create value: {0} in domain Description: {1}'.format(valeDoaminRow[1],valeDoaminRow[2]) 
# Process: Constrain the material value of distribution mains
        # arcpy.AssignDomainToField_management(inFeatures, inField, domName)
        # print 'create domain in field'