# Modified version of the script from 
# https://stackoverflow.com/questions/36155049/splitting-xml-file-into-multiple-at-given-tags

import xml.etree.ElementTree as ET
context = ET.iterparse('', events=('end', )) #big file path
for event, elem in context:
    if elem.tag == 'transcript': #Split by tag
        data = ET.tostring(elem,encoding='UTF-8')
        file_name_tmp = re.search('\d\d-\d\d-\d\d.xml',data.decode(encoding='UTF-8')) #Search docname by pattern and use as file name
        filename = file_name_tmp.group(0)
        with open(filename, 'wb') as f:
            f.write(data)