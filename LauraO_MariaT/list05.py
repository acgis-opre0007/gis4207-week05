import sys
import os

def main():
    
    if len(sys.argv) !=2:
        print ("Usage:List05.py <root_folder>")
        sys.exit()
    
    rootFolder = sys.argv[1]
    
    if not os.path.exists(rootFolder):
        print ("The root_folder does not exist")
        sys.exit()
    
    get_folder(rootFolder)     

def get_folder(rootFolder):
    for root, dirs, files in os.walk(rootFolder):
        for d in dirs:
                print(os.path.join(root, d))       
        
if __name__ == "__main__":
        main ()



