import sys
import os

def main():
    global arcpy 
    
    if len(sys.argv) !=4:
        print ("Usage:List08.py <root_folder> <Point|Polyline|polygon> <out_file_name>")
        sys.exit()
    
    rootFolder = sys.argv[1]
    feature_type = sys.argv[2]
    out_file = sys.argv[3]
    
    import arcpy
    
    if not os.path.exists(rootFolder):
        print ("The root_folder does not exist")
        sys.exit()
    
    if not arcpy.da.Walk(rootFolder, datatype='FeatureClass'):
        print ("The file does not contain a feature class")
        sys.exit()
    
    get_workspace_folder(rootFolder, feature_type, out_file)     

#TO DO: not working at the moment

def get_workspace_folder(rootFolder, feature_type, out_file):
    for root, dirs, files in arcpy.da.walk(rootFolder, datatype='FeatureClass', type=['Point', 'Polyline', 'Polygon']):
        arcpy.env.workspace = root
        workspace_list = arcpy.ListWorkspaces()
        for workspace in workspace_list:
            arcpy.env.workspace = workspace
            fc_list = arcpy.ListFeatureClasses()
            for fc in fc_list:
                if arcpy.Describe(fc).shapeType == feature_type:
                 print (os.path.abspath(workspace),fc)
                 
        with open(out_file, "w") as out_file:
            out_file.writer(f'{feature_type} feature classes in and below {rootFolder}')
            for fc in fc_list:
                out_file.write(fc)
      
        
if __name__ == "__main__":
        main ()