#Search by Section name and copy all the xml files with the specific session to new location.
#Information of the session name and count are logged in CSV file
#For instance, if <MotionSections> need to be updated, run the script with <MotionSection> in pattern
#The script will copy all the xml files with Motion Section to new location. Do all the stuff in new location 
# and if everything is fine, merge with the main repo.
import csv 
import pathlib
import re
import pandas as pd
import os
import shutil
import pandas as pd

amyotha_path = ''#Path to amyotha files
pyithu_path = ''#Path to pyithu files

#Update Parameters Here
absolute_path = pyithu_path #Update absolute path here
pattern1 = r'' #Put Section name Here
distinct_column = pattern1

path = pathlib.Path(absolute_path)
copy_path = '' #Output directory path

records = []
for p in path.rglob('*.xml'):
    print("Processing {}".format(p.absolute()))
    with open(p.absolute(), 'r',encoding='UTF-8') as file :
        filedata = file.read()
    filename = p.stem
    p1 = int(len(re.findall(pattern1,filedata)))
    records.append([filename,p1])
    df = pd.DataFrame(records, columns=['file_name', pattern1])

df.to_csv('') #Path to output CSV
file_list = df.file_name.tolist()
file_names = [x+'{}'.format('.xml') for x in file_list]

for root, dirs, files in os.walk(absolute_path):
    for _file in files:
        if _file in file_names:
            # if found, notify and copy to defined path
            print ('Found file in: ' + str(root))
            shutil.copy(os.path.abspath(root + '/' + _file), copy_path )




