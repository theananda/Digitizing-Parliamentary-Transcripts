#Iterate through all the lines and search a pattern
#if the pattern was found, the string will put inside XML Tag
import re
import pandas as pd
import csv

df = pd.read_csv('', header=None)#Path to data file
df.columns = ['text'] #rename the column to "text"
pattern = r"^ဦး.*မဲဆန္ဒနယ်\)။ ။"   #specify the pattern here #RUN AGAIN WITH ပါတယ်

#Possible start of the sentence
find_1 = "ဦး"
replace_1 = "<speaker>"

#Possible end of the sentence
find_2 = "ဖြစ်ပါတယ်။"
replace_2 = "ဖြစ်ပါတယ်။</speaker>"

for x in df.text:
    new_df=[]
    if re.search(pattern,x) is None:
        new_df.append(x)
    else:
        original_string = str(re.findall(pattern,x))
        x = re.sub(find_1,replace_1,original_string)
        new_string = re.sub(find_2,replace_2,x)
        new_string = ''.join(new_string)
        new_df.append(new_string)
    with open('output.csv','a') as file:
        w = csv.writer(file, quoting=csv.QUOTE_ALL)
        w.writerow(new_df)



