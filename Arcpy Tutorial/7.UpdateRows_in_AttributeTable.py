import arcpy

ports= r'C:\Users\L\Downloads\Compressed\SHP for Arcpy\Ports.shp'

with arcpy.da.UpdateCursor(ports,['Test_attri']) as portsCurosr:
  for x in portsCurosr:
    print x[0]
    x[0] = 'We_Just_Update_Test'
    portsCurosr.updateRow(x)
    print "We update this value to {}".format(x[0])

print 'Finish'