import requests
import os
URL = "https://cloud-api.yandex.net/v1/disk/resources/upload"

headers = {

    "Authorization" : "OAuth AgAAAAAiq3TDAADLWyDQpGaceEuJs63ZFtIoVy0"
}
params = {
    
    "path": "files",
    "overwrite": "True"
}

try:
    resp= requests.get(URL,headers=headers,params=params)
    resp.raise_for_status()
    print(resp.json())
except Exception as e:
    print(e)
