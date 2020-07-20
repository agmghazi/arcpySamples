import arcpy
arcpy.env.overwriteOutput = True


ports= r'C:\Users\L\Downloads\Compressed\SHP for Arcpy\Ports.shp'
timeZone= r'C:\Users\L\Downloads\Compressed\SHP for Arcpy\TimeZone.shp'
output = r'C:\Users\L\Downloads\Compressed\SHP for Arcpy\Outputs'
PortsName = ['Iran','New_Zealand','Falkland_Islands','Halley_Station']

with arcpy.da.SearchCursor(ports,['featurecla','scalerank','website','name']) as portsData:
  for x in portsData:
    print x[0]
    print x[1]
    print x[2]
    print x[3] +'\n'
    