import sys
import os

def main():
    global arcpy 
    
    if len(sys.argv) !=2:
        print ("Usage:List06.py <root_folder>")
        sys.exit()
    
    rootFolder = sys.argv[1]
    
    import arcpy 
    
    if not os.path.exists(rootFolder):
        print ("The root_folder does not exist")
        sys.exit()
    
    get_workspace_folder(rootFolder)     

def get_workspace_folder(rootFolder):
    for root, dirs, files in os.walk(rootFolder):
        arcpy.env.workspace = root
        workspace_list = arcpy.ListWorkspaces()
        for workspace in workspace_list:
            arcpy.env.workspace = workspace
            fc_list = arcpy.ListFeatureClasses()
            for fc in fc_list:
                 print (os.path.abspath(workspace),fc)
      
        
if __name__ == "__main__":
        main ()



