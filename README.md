# Digitizing-Parliamentary-Transcripts
Scripts Used in data wrangling and structuring Parliamentary Transcripts

### id_matcher.py
Search possible text pattern and match with the patterm from dataset. If they are above similarity threshold, id of the mp is added.

### copy_files_by_keyword.py
Search by Section name and copy all the xml files with the specific session to new location. Information of the session name and count are logged in CSV file

### mm_text_nomalizer.py
Normalize typos and spelling errors cause by OCR.

### walker.py
Iterate through specific directory replace keywords

### validate.py
Iterate all the xml files in the directory parse, validate and make a csv dictionary

### search_replace.py
Iterate through all the lines and search a pattern in the text file. If the pattern was found, the string will put inside XML Tag

### concat.py
Quick and dirty script to combine text files

### xml_splitter.py
Split big xml file into small xml files by tag

### downloader.py
Small script to download multiple files using wget module
