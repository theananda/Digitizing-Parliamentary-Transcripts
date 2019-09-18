#Search possible pattern with regex in the data file
#Match the mp name with the name from mp dataset
#If they are above similarity threshold, update to data file.
#fuzzywuzzy use Levenshtein Distance to calculate the differences between sequences.
#https://github.com/seatgeek/fuzzywuzzy
import pandas as pd
import re
from fuzzywuzzy import fuzz
import csv

df = pd.read_csv('') #Path to data file
df.columns = ['text']

df2 = pd.read_csv('') #Path to csv file with mp names and ids

pattern = "" #Update regex pattern accordingly

#regex for pyithu
#pattern = r"^(\u1026\u1038|\u1012\u1031\u102B\u103A|\u1012\u1031\u102B\u1000\u103A\u1010\u102C)(.*?)(\u1019\u1032\u1006\u1014\u1039\u1012\u1014\u101A\u103A\)\u104B \u104B)"
#regex for amyotha
#pattern = r"^(\u1026\u1038|\u1012\u1031\u102B\u103A|\u1012\u1031\u102B\u1000\u103A\u1010\u102C)(.*?)(\u1019\u1032\u1006\u1014\u1039\u1012\u1014\u101A\u103A\u1021\u1019\u103E\u1010\u103A\(.+\)\u104B \u104B)"
#regex for Ministers
#pattern = r"^(\u1026\u1038|\u1012\u1031\u102B\u103A}|\u1012\u1031\u102B\u1000\u103A\u1010\u102C})(.*?)(\u101D\u1014\u103A\u1000\u103C\u102E\u1038\u100C\u102C\u1014\)\u104B \u104B)"

#Update the tags accordingly
#Possible tags <mp> <agency>
def tag_constructor(mp_name, mp_id):
    xml_tag = '<mp id=\'{}\'>{}</mp>'.format(mp_id,mp_name)
    return xml_tag

#Compare two values and if the value is above similarity threshold id is substituted
#id will be given UNKNOWN if it's under similarity threshold
#Need inspect and fix UNKNOWN keywords later
def id_matcher(mp_name_original,x):
    for mp_id,mp_name_csv in zip(df2.id,df2.mp_name):
        if fuzz.ratio(mp_name_original,mp_name_csv)>=95:  
            replace_string = tag_constructor(mp_name_original,mp_id)
            final_string = x.replace(mp_name_original,replace_string)
            return final_string
    else:
        replace_string = tag_constructor(mp_name_original,'UNKNOWN')
        final_string = x.replace(mp_name_original,replace_string)
        return final_string


def main():
    for x in df.text:
    new_df=[]
    if re.search(pattern,x) is None:
        new_df.append(x)
    else:
        temp_var = re.match(pattern,x)  #match the pattern
        mp_name_original = temp_var.group(0) #put the name in the list
        new_df.append(id_matcher(mp_name_original,x))
        
    with open('output2.csv','a') as file:
            w = csv.writer(file, quoting=csv.QUOTE_ALL)
            w.writerow(new_df)

if __name__ == '__main__':
    main()



