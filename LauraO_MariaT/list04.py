import sys

def main():
    
    if len(sys.argv) !=2:
        print ("Usage:List04.py <FeatureClassName>")
        sys.exit()
    
#TO DO: 
    file = r'..\..\..\..\data'
    #sys.argv[1]

    import arcpy
    from arcpy import env
    
    arcpy.env.workspace = file
  
    des_FC = arcpy.ListWorkspaces()
    for f in des_FC:
        print(f)    
        
    if not arcpy.Exists(file):
        print("The feature class does not exist.")
        sys.exit()

if __name__ == "__main__":
        main ()