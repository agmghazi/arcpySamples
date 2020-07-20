import arcpy
arcpy.env.overwriteOutput = True


ports= arcpy.GetParameterAsText(0)
timeZone = arcpy.GetParameterAsText(1)
output = arcpy.GetParameterAsText(2)
pop_number = arcpy.GetParameterAsText(3)

total_count = 0
created_count =0

arcpy.MakeFeatureLayer_management(ports,'ports_layer')

with arcpy.da.SearchCursor(timeZone,['FID','dst_places','map_color8']) as timeZonesData:
  for x in timeZonesData:
    total_count +=1

    if x[2] > float(pop_number):
      created_count +=1
      print x[1]
      arcpy.MakeFeatureLayer_management(timeZone,'timeZone_layer' ,""" "FID"= {} """.format(x[0]))
      arcpy.SelectLayerByLocation_management('ports_layer','WITHIN','timeZone_layer')
      formatted_output_name = x[1].replace('(','_').replace(')','_').replace(',','_').replace('&','_')
      arcpy.FeatureClassToFeatureClass_conversion('ports_layer',output,'port_in_{0}_{1}'.format(formatted_output_name,x[0]))
      print 'Successfully Converted {} \n'.format(formatted_output_name)
      arcpy.AddMessage('Successfully Converted {} \n'.format(formatted_output_name))
    else:
      print "{} didnt met the timeZone".format(x[1])
      arcpy.AddMessage("{} didnt met the timeZone".format(x[1]))

print 'Finish'
arcpy.AddMessage('Finish')
print "{0} created the timeZone out of {1} TimeZones".format(created_count,total_count)
arcpy.AddMessage("{0} created the timeZone out of {1} TimeZones".format(created_count,total_count))   

    