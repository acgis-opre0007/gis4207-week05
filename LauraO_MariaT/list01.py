import arcpy
from arcpy import env

env.workspace = r'..\..\..\..\data\SanFrancisco'

des_FC = arcpy.ListFeatureClasses()

for fc in des_FC:
    print(fc)
    