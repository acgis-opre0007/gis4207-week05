import arcpy.da
import sys

def main():
    
    if len(sys.argv) !=2:
        print ("Usage:describe03.py <FeatureClassName>")
        sys.exit()
        
    file = sys.argv[1]
    # file = r'..\..\..\..\data\Canada\province.shp'
    desc_dic= arcpy.da.Describe(file)

#print(type(desc_dic))
#print(desc_dic.keys())
    print(desc_dic['baseName'])
    print(desc_dic['catalogPath'])
    print(desc_dic['dataType'])


if __name__ == "__main__":
        main ()