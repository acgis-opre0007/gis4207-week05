import sys
import os

def main():
    global arcpy 
    
    if len(sys.argv) !=4:
        print ("Usage:List08.py <root_folder> <Point|Polyline|Polygon> <out_file_name>")
        sys.exit()
    
    rootFolder = sys.argv[1]
    feature_type = sys.argv[2]
    out_file = sys.argv[3]
    
    import arcpy.da
    
    if not os.path.exists(rootFolder):
        print ("The root_folder does not exist")
        sys.exit()
    
    if not arcpy.da.Walk(rootFolder, datatype='FeatureClass'):
        print ("The file does not contain a feature class")
        sys.exit()
    
    get_da_walker(rootFolder, feature_type, out_file)     

#TO DO: not working at the moment

def get_da_walker(rootFolder, feature_type, out_file):
    feat_class = []
    walk = arcpy.da.Walk(rootFolder, datatype='FeatureClass', type="feature_type")

    for dirpath, dirnames, filenames in walk:
        for filename in filenames:
            feat_class.append(os.path.join(dirpath, filename))  
    
    with open(out_file, "w") as file:
            file.write(f'{feature_type} feature classes in and below {os.path.abspath(rootFolder)}')
            for fc in feat_class:
                file.write(fc)
      
    #for root, dirs, files in arcpy.da.walk(rootFolder, datatype='FeatureClass', type=['Point', 'Polyline', 'Polygon']):
        #arcpy.env.workspace = root
        #workspace_list = arcpy.ListWorkspaces()
        #for workspace in workspace_list:
            #arcpy.env.workspace = workspace
            #fc_list = arcpy.ListFeatureClasses()
            #for fc in fc_list:
                #if arcpy.Describe(fc).shapeType == feature_type:
                    #print (os.path.abspath(workspace),fc, feature_type)
        
if __name__ == "__main__":
        main ()