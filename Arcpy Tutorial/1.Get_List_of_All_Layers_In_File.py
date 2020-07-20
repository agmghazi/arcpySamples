import arcpy

try:
 arcpy.env.workspace = r'C:\Users\L\Downloads\Compressed\SHP for Arcpy'
 feature_List=arcpy.ListFeatureClasses()
 print feature_List

except:
   print(arcpy.GetMessages())
