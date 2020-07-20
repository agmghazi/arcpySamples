import arcpy

try:
 ports= r'C:\Users\L\Downloads\Compressed\SHP for Arcpy\Ports.shp'
 timeZone= r'C:\Users\L\Downloads\Compressed\SHP for Arcpy\TimeZone.shp'
 output = r'C:\Users\L\Downloads\Compressed\SHP for Arcpy\Outputs'


 arcpy.MakeFeatureLayer_management(ports,'ports_layer')
 arcpy.MakeFeatureLayer_management(timeZone,'timeZone_layer' ,""" "dst_places"='Falkland Islands' """)

 arcpy.SelectLayerByLocation_management('ports_layer','WITHIN','timeZone_layer')
 arcpy.FeatureClassToFeatureClass_conversion('ports_layer',output,'ports_Extract')

except:
   print(arcpy.GetMessages())
