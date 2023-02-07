import arcpy
import os
import sys

def main():
    
    if len(sys.argv) !=1:
        print ("Usage:  describe03.py <FeatureClassName>")
        sys.exist()
    else:
        print("Error turn back")

file = r'..\..\..\..\data\Canada\province.shp'
desc = arcpy.da.Describe(file)

print(f'{"Basename":13}{desc.BaseName}')
print(f'{"Catalog":13}{desc.catalogPath}')
print(f'{"Datatype":13}{desc.dataType}')

if __name__ == '__main__':
        main ()