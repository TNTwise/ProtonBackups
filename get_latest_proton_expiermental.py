#!/usr/bin/python

#IMPORTANT !!!!!!!!!!!!!!!!!!!
# You need to be enrolled in the proton expiermental beta for this to work, otherwise it will just get the latest expiermental non-bleeding edge

from genericpath import isfile
import os
import csv
from posixpath import expanduser
import re
home_dir = expanduser("~")

# This code extracts the build version of proton

f = open(home_dir+"/.local/share/Steam/steamapps/common/Proton - Experimental/version", "r")
f = csv.reader(f)
for row in f: 
    build_num = row
proton_ver = ""
for value in row:
    proton_ver = value
proton_ver = re.findall("-[\d].[\d]-[\d]*", proton_ver)
for value in proton_ver:
    proton_ver = value

proton_ver = "ExBE" + proton_ver
proton_dir = home_dir+'/Downloads/'+proton_ver+'/'+proton_ver

#Checks to see if the proton version has already been copied, this prevents errors.
if os.path.isfile(home_dir+'/Downloads/' + proton_ver+"/proton") == True:
    print("This version has already been extracted.")
else:
    os.system("mkdir /home/$USER/Downloads/" + proton_ver)
    os.system('cp -r /home/$USER/.local/share/Steam/steamapps/common/Proton\ -\ Experimental/* /home/$USER/Downloads/' + proton_ver+'/')


    # This code changes the values within the files to match the proton version.
    temp_list = []

    with open(home_dir+'/Downloads/'+proton_ver+'/'+"/compatibilitytool.vdf", "w") as f:
        f.write('"compatibilitytools"\n')
        f.write("{\n")
        f.write('  "compat_tools"\n')
        f.write('  {\n')
        f.write('    "'+proton_ver +'"'+' // Internal name of this tool  \n')
        f.write('    {\n')
        f.write('      "install_path" "."\n')
        f.write('      "display_name"' +' "'+proton_ver+'"\n')
        f.write('      "from_oslist"  "windows"\n')
        f.write('      "to_oslist"    "linux"\n')
        f.write('    }\n')
        f.write('  }\n')
        f.write('}\n')

    temp_list = []

    # this will change the proton previx version within the proton file

    with open(home_dir+'/Downloads/'+proton_ver+'/'+"/proton", "r") as f:
        for line in f:
            temp_list.append(line) # Creates a list of all the lines within the proton file.

    temp_list[42] = 'CURRENT_PREFIX_VERSION="'+proton_ver+'"'

    # This will write the changes to the file

    with open(home_dir+'/Downloads/'+proton_ver+'/'+"/proton", "w") as f:
        for value in temp_list:
            f.write(value)

    #this code will ask the user if they want to zip it
    #This is dumb
    isCompress = input("Do you want to compress it? (y / n): ")
    if isCompress == "y":
        os.chdir(home_dir+'/Downloads')
        os.system('zip  -b '+home_dir+'/Downloads/ -r -y '+proton_ver+'.zip  '+proton_ver+'/*')