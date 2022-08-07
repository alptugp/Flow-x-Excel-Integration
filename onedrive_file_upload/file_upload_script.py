import os
import requests 
from ms_graph import generate_access_token, GRAPH_API_ENDPOINT

APP_ID = 'a62b7597-8acf-43ea-97a4-38d2b1173c5b'
SCOPES = ['Files.ReadWrite']

access_token = generate_access_token(APP_ID, SCOPES)
headers = {
    'Authorization': 'Bearer ' + access_token['access_token']
}

file_path = r'/Users/alptug/Desktop/Flow-x-Excel-Integration/onedrive_file_upload/example'
file_name = os.path.basename(file_path)
  
with open(file_path, 'rb') as upload:
    media_content = upload.read()

response = requests.put(
    GRAPH_API_ENDPOINT + f'/me/drive/items/root:/{file_name}:/content',
    headers=headers,
    data=media_content
)
print(response.json())

