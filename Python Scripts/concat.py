#Quick and dirty script to Read all the text files in the directory and concat them into one big file
#Filename is use as seprator between files

import os

lst = os.listdir("")
final_output = "" 

with open(final_output, 'w') as outfile:
    for fname in sorted(lst):
        with open("./Text/"+fname) as infile:
            outfile.write("\n<"+fname+">\n")
            outfile.write(infile.read())
            outfile.write("\n</"+fname+">\n")





