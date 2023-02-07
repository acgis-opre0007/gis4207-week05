import arcpy
import os

file = r'..\..\..\..\data\Canada\province.shp'
desc = arcpy.Describe(file)

print(f'{"Basename":13}{desc.BaseName}')
print(f'{"Catalog":13}{desc.catalogPath}')
print(f'{"Datatype":13}{desc.dataType}') 
 