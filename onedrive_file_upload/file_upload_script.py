import os
import requests 
from ms_graph import generate_access_token, GRAPH_API_ENDPOINT

APP_ID = '8a3c7beb-e11d-4ea4-a75f-b57c7a68cea9'
SCOPES = ['Files.ReadWrite']

access_token = generate_access_token(APP_ID, SCOPES)
headers = {
    'Authorization': 'Bearer ' + access_token['access_token']
}


 