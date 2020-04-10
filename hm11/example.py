import requests
import os
from pathlib import Path
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def upload(text,filename):
    URL= "https://cloud-api.yandex.net/v1/disk/resources/upload"
    headers = {
      
        "Authorization" : "OAuth AgAAAAAiq3TDAADLWyDQpGaceEuJs63ZFtIoVy0",
        
    }
    params = {
        "path": f"files/{filename}",
        "overwrite": "True"
    }
    try:
        resp= requests.get(URL,headers=headers,params=params)
        resp.raise_for_status()
    except Exception as e:
        print(e)

    href = resp.json()['href']
    resp = requests.put(href,headers=headers, data=text.encode("utf-8"),params=params)

def translate_it(from_file_path,to_file_path,from_lang, to_lang="ru",):
    with open(from_file_path, encoding="UTF-8") as f:
        text = f.read()
        

    

    params = {
        'key': API_KEY,
        'text': text,
        'lang': f'{from_lang}-{to_lang}'
    }
    filename = f"{from_lang}.txt"
    response = requests.get(URL, params=params)
    json_ = response.json()
    try:
        os.mkdir(to_file_path)
        to_file_path = os.path.join(to_file_path,filename)
    except:
        to_file_path = os.path.join(to_file_path,filename)
            
    with open(to_file_path, 'w', encoding="UTF-8") as file:
        
            file.write(json_["text"][0])

    with open(to_file_path, encoding='UTF-8' ) as f:
        show_text = f.read().strip()
        upload(show_text,filename)
        
    return show_text
if __name__ == '__main__':
    print(translate_it("DE.txt","fcreat", "de","en"))
    print(translate_it("FR.txt","fcreat", 'fr'))
    print(translate_it("ES.txt","fcreat", 'es'))
    print( "\n ссылка на папку \n",requests.get("https://cloud-api.yandex.net/v1/disk/resources/public",headers={"Authorization" : "OAuth AgAAAAAiq3TDAADLWyDQpGaceEuJs63ZFtIoVy0"}).json()['items'][0]['public_url'])