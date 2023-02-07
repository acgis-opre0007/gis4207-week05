import arcpy
import os

file = r'..\..\..\..\data\Canada\province.shp'
desc = arcpy.Describe(file)

print(f'Basename:{desc.BaseName}')
print(f'Catalog:{desc.catalogPath}')
print(f'Datatype:{desc.dataType}') 
 