import sys

def main():
    global arcpy, env
    
    
    if len(sys.argv) !=2:
        print ("Usage:describe03.py <FeatureClassName>")
        sys.exit()
        
    file = sys.argv[1]
    
    import arcpy

    if not arcpy.Exists(file):
        print("The feature class " + file + " does not exist.")
        sys.exit()
        
    feature_class(file)
    
    
def feature_class(file):
    
    dsc = arcpy.Describe(file)
    print (dsc.name)


if __name__ == "__main__":
        main ()