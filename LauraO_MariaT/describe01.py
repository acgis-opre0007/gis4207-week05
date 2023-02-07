import arcpy
import os

file = r'..\..\..\..\data\Canada\province.shp'
desc = arcpy.Describe(file)

print("Basename" : {desc.name})
print("Catalog" :{desc.catalogPath})
print("Datatype": {desc.dataType}) 
