import sys

def main():
    
    if len(sys.argv) !=2:
        print ("Usage:List02.py <FeatureClassName>")
        sys.exit()
    
    file = sys.argv[1]
    
    import arcpy
    from arcpy import env


    if not arcpy.Exists(file):
        print("The feature class does not exist.")
        sys.exit()
            
    arcpy.env.workspace = file
    
    des_FC = arcpy.ListFeatureClasses()
    for fc in des_FC:
         print(fc)    


if __name__ == "__main__":
        main ()