import os
import re
def sorted_alphanumeric(data):
    #https://stackoverflow.com/a/48030307
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)
list = ""
os.chdir("resources")
for file in sorted_alphanumeric(os.listdir()):
    #print(file)
    if file.endswith(".gif"):
        list+="![Pokemon](resources/"+file+") "
        
os.chdir("..")
f = open("README.md","w")
f.write("# DAIN-crystal-pokemon\n")
f.write(list)
print(f)
f.close()
#print(list)