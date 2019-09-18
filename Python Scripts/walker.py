# Script iterate through specific directory replace keywords
import os
from glob import glob
import pathlib
import collections
import csv
import xml.etree.ElementTree as et

#Path to xml or text files
abs_path = ''
path = pathlib.Path(abs_path)

for p in path.rglob('*.xml'):
    print("Processing {}".format(p.absolute()))
    with open(p.absolute(), 'r',encoding='UTF-8') as file :
        filedata = file.read()
        filedata = filedata.replace('<mc>',"<speech type='mc'>")#('find','replace')
        filedata = filedata.replace('</mc>','</speech>')#('find','replace')
    with open(p.absolute(),'w',encoding='UTF-8') as file:
        file.write(filedata)



