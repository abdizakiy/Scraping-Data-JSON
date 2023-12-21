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
        url.lstrip('https://').split('/')[0].strip()+'.csv', 
        index=False)
    
    break

    
#     for x in container:
#         name = x.find("h5", class_="margin-two text-center").text
#         list_nama.append(name)
        
#         try : location = x.find("p", class_="text-uppercase no-margin-bottom").text
#         except : location = ""
#         list_lokasi.append(location)
        
#         try : floor = x.find("h6", class_="no-margin-top margin-two-bottom").text
#         except : floor = ""
#         list_lantai.append(floor)

#         try : profile = x.find_all("a", class_="highlight-button-dark btn btn-very-small margin-three no-margin")
#         except : profile = ""
#         for y in profile:
#             linktoko = y.get('href')
#             list_profil.append(y.get('href'))


#         toko_req        = requests.get(linktoko)
#         toko_soup       = BeautifulSoup(toko_req.text, "html.parser")
#         toko_container  = toko_soup.find_all("div", class_="col-md-5 col-sm-12 col-md-offset-1 padding-two-bottom")

#         for y in toko_container:
#             product = y.find(text='product').find_next('p').text
#             list_produk.append(product)

#             try : park = y.find(text='where to park').find_next('p').text
#             except : park = ""
#             list_parkir.append(park)

#             try : contact = y.find("a", class_="btn-phone")
#             except : contact = ""
#             if contact is None:
#                 list_kontak.append("")
#             else :
#                 list_kontak.append(contact.get('href')[4:])

#             whatsapp = y.find("a", class_="btn-wa")
#             if whatsapp is None:
#                 list_wa.append("")
#             else :
#                 list_wa.append(whatsapp.get('href'))
            

#         try : image = x.find_all("img")
#         except : image = ""
#         for x in image:
#             # print(x.get('src'))
# #             # print(x.get('src'))
#             list_gambar.append(x.get('src'))


