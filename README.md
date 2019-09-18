# Digitizing-Parliamentary-Transcripts
Scripts Used in data wrangling and structuring Parliamentary Transcripts

##id_matcher.py
Search possible text pattern and match with the patterm from dataset. If they are above similarity threshold, id of the mp is added.

##walker.py
Iterate through specific directory replace keywords

##validate.py
Iterate all the xml files in the directory parse, validate and make a csv dictionary

##search_replace.py
Iterate through all the lines and search a pattern in the text file. If the pattern was found, the string will put inside XML Tag

##concat.py
Quick and dirty script to combine text files
