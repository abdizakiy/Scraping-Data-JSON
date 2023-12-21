import requests
from bs4 import BeautifulSoup
import pandas as pd
from fake_useragent import UserAgent

url = 'https://app.chargespot.jp/map/data.json?new2&_=1696492143987'
headers = {'user-agent': UserAgent().random}
list_nama    = []
list_lat  = []
list_lon  = []
idx = 0

while True:
    print("scanning page...")
    print(url)
    req = requests.get(url, headers=headers)
    json = req.json()
    total = len(json)
    for x in json:
        print(x)
        list_nama.append(x[0])
        list_lat.append(x[1])
        list_lon.append(x[2])
        
        idx += 1
        print(idx, "/", total, x[0], [x[1], x[2]])

    data = pd.DataFrame(list(zip(
        list_nama, 
        list_lat, 
        list_lon)), 
        
        columns=[
            'Nama', 
            "Latitude", 
            "Longitude"])
    
    data.to_csv(
        url.lstrip('https://www.').split('/')[0].replace('.', '_').strip()+'.csv', 
        index=False)
    
    break