import sys

def main():
    global arcpy, env
    
    
    if len(sys.argv) !=2:
        print ("Usage:describe03.py <FeatureClassName>")
        sys.exit()
        
    file = sys.argv[1]
    
    import arcpy
        
    feature_class(file)
    
    
def feature_class(file):
    
    dsc = arcpy.Describe(file)
    print(f'{"Basename":13}{dsc.BaseName}')
    print(f'{"Catalog":13}{dsc.catalogPath}')
    print(f'{"Datatype":13}{dsc.dataType}')


if __name__ == "__main__":
        main ()