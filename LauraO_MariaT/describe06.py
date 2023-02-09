import sys

def main():
    global arcpy, env
    
    if len(sys.argv) !=2:
        print ("Usage:describe03.py <FeatureClassName>")
        sys.exit()
        
    file = sys.argv[1]
    
    import arcpy.da

    if not arcpy.Exists(file):
        print("The feature class " + file + " does not exist.")
        sys.exit()
        
    feature_class(file)
    
def feature_class(file):
    
    dic_dsc = arcpy.da.Describe(file)
    print(f"{dic_dsc['baseName']:15}{type(dic_dsc['baseName']).__name__:15}{len(dic_dsc['baseName']):>9}")
    print(f"{dic_dsc['catalogPath']:15}{type(dic_dsc['catalogPath']).__name__:15}{len(dic_dsc['catalogPath']):>9}")
    print(f"{dic_dsc['dataType']:15}{type(dic_dsc['dataType']).__name__:15}{len(dic_dsc['dataType']):>9}")

if __name__ == "__main__":
        main ()