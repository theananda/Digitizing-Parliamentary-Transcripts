#Iterate all the xml files in the directory parse, validate and make a csv dictionary
#If there's parse error, file name with with the error will printed and need to recheck manually
import os
from glob import glob
import pathlib
import collections
import csv
import xml.etree.ElementTree as et

#Path to xml files
abs_path = ''
path = pathlib.Path(abs_path)

for p in path.rglob('*.xml'):
    print("Processing {}".format(p.absolute()))
    try:
        tree = et.parse(p.absolute())
        root = tree.getroot()
        for elem in root:
            element =elem.tag
            with open('map.csv',mode='a') as file:
                w = csv.writer(file)
                w.writerow([element,p.stem])
    except ParseError:
        print('{} has error'.format(p.stem))

