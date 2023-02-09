import sys

def main():
    global arcpy, env
    
    
    if len(sys.argv) !=2:
        print ("Usage:describe03.py <FeatureClassName>")
        sys.exit()
        
    file = sys.argv[1]
    
    import arcpy.da

    if not arcpy.Exists(file):
        print("The feature class does not exist.")
        sys.exit()
        
    feature_class(file)
    
    
def feature_class(file):
    
    dic_dsc = arcpy.da.Describe(file)
    print(dic_dsc['baseName'])
    print(dic_dsc['catalogPath'])
    print(dic_dsc['dataType'])


if __name__ == "__main__":
        main ()