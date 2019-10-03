import pandas as pd
import wget
import ssl #In case if there's SSL error
ssl._create_default_https_context = ssl._create_unverified_context
df = pd.read_csv('') #CSV file path
for url in df['']: #download link column name
    try:    
        wget.download(url)
        time.sleep(randint(4,10))
    except:
        print(f'Error on {url}')
        pass