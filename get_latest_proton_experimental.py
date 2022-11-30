#!/usr/bin/python

#IMPORTANT !!!!!!!!!!!!!!!!!!!
# You need to be enrolled in the proton expiermental beta for this to work, otherwise it will just get the latest expiermental non-bleeding edge

from genericpath import isfile
import os
import csv
from posixpath import expanduser
import re
home_dir = expanduser("~")
cwd = os.getcwd() 

def get_proton_ver():
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
    temp_num = 0 #This is set to count the amount of letters in the proton version, and if there is more than 9, it will be set as a proton experimental non bleeding edge version.
    for i in proton_ver:
        temp_num +=1
    if temp_num < 12:
        proton_ver = "ExBE" + proton_ver
    else:
        proton_ver = "Ex" + proton_ver
    return proton_ver
proton_ver = get_proton_ver()
# This code extracts the build version of proton


proton_dir = home_dir+'/Downloads/'+proton_ver+'/'+proton_ver

# This code saves the latest version of proton in a file, and if it does exist, it reads the file and gets the last proton version
if os.path.isfile(cwd+"/proton_last_ver") == False:
    os.mknod(cwd+"/proton_last_ver")
else:
    f = open(cwd+"/proton_last_ver")
    f = csv.reader(f)
    for row in f:
        proton_last_ver = row


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
print("Extracted Successfuly.")
isCompress = input("Do you want to compress it? (y / n): ")
isCompress = isCompress.lower()
if isCompress == "y":
    if os.path.isfile(home_dir+'/Downloads/'+proton_ver+'.zip') == False:
        os.chdir(home_dir+'/Downloads')
        os.system('zip  -b '+home_dir+'/Downloads/ -r -y '+proton_ver+'.zip  '+proton_ver+'/*')
    else:
        print("You have already compressed this version.")

    # Asks the user if they would like to automatically move it to the compat folder.
    
isMove = input("Would you like to move the extracted version to the 'compatibilitytools.d' folder? (y / n): ")
isMove = isMove.lower()
if isMove == "y":
    if os.path.isfile(home_dir+"/.steam/steam/compatibilitytools.d/"+proton_ver+"/proton") == False:
            os.system("mv "+home_dir+"/Downloads/"+proton_ver+" "+home_dir+"/.steam/steam/compatibilitytools.d/")
    else:
        print("The version you have extracted already exists in the compatibilitytools.d folder.")
        isdel_1 = input("Do you want to delete the extracted version? (y / n): ")
        isdel_1 = isdel_1.lower()
        if isdel_1 == "y":
            os.system("rm -f"+home_dir+"/Downloads/"+proton_ver)
if isMove == "n": 
    isdel_1 = input("Do you want to delete the extracted version? (y / n): ")
    isdel_1 = isdel_1.lower()
    if isdel_1 == "y":
        os.system("rm -f"+home_dir+"/Downloads/"+proton_ver)

if os.path.isfile(cwd+"/proton_last_ver") == True:
    # This will ask you if you want to delete the previous version
    is_del_last_ver = input("Do you want to delete the last version? (y / n): ")
    if is_del_last_ver.lower() == "y":
        os.system("rm -rf "+home_dir+"/.steam/steam/compatibilitytools.d/"+proton_ver+"/")


# This code will overwrite the file with the current version of proton
with open(cwd+"/proton_last_ver", "w") as f:
    f.write(proton_ver)






