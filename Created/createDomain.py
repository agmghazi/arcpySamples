import arcpy
 
try:
    # Set the workspace (to avoid having to type in the full path to the data every time)
    arcpy.env.workspace = r"D:\filetest\out"
 
    # Set local parameters
    domName = "Material"
    gdb = "AmanaGDB.gdb"
    inFeatures = "AmanaGDB.gdb\Setage\FC_Point"
    inField = "Name"
 
    # Process: Create the coded value domain
    arcpy.CreateDomain_management("AmanaGDB.gdb", domName, "Description of Doamin Name", "TEXT", "CODED")
    print 'create Domain'

    #Store all the domain values in a dictionary with the domain code as the "key" and the 
    #domain description as the "value" (domDict[code])
    domDict = {"CI":"Cast iron", "DI": "Ductile iron", "PVC": "PVC", \
                "ACP": "Asbestos concrete", "COP": "Copper"}
    
    # Process: Add valid material types to the domain
    #use a for loop to cycle through all the domain codes in the dictionary
    for code in domDict:        
        arcpy.AddCodedValueToDomain_management(gdb, domName, code, domDict[code])
    print 'create valuein domain'    
    # Process: Constrain the material value of distribution mains
    arcpy.AssignDomainToField_management(inFeatures, inField, domName)
    print 'create domain in field'
except Exception as err:
    print(err.args[0])
