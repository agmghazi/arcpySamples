import arcpy
arcpy.env.overwriteOutput = True

ports= r'C:\Users\L\Downloads\Compressed\SHP for Arcpy\Ports.shp'
timeZone= r'C:\Users\L\Downloads\Compressed\SHP for Arcpy\TimeZone.shp'
output = r'C:\Users\L\Downloads\Compressed\SHP for Arcpy\Outputs'
PortsName = ['Iran','New_Zealand','Falkland_Islands','Halley_Station']

arcpy.MakeFeatureLayer_management(ports,'ports_layer')

for result in PortsName:
  print result
  arcpy.MakeFeatureLayer_management(timeZone,'timeZone_layer' ,""" "dst_places"='{}' """.format(result))
  arcpy.SelectLayerByLocation_management('ports_layer','WITHIN','timeZone_layer')
  arcpy.FeatureClassToFeatureClass_conversion('ports_layer',output,'port_{}'.format(result))
