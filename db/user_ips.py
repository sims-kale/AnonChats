import requests

AIRTABLE_API_KEY = 'patP5LW5mVIcN5cij.8f1c28c482b9d10ee4cf33ed2d55bbc76f1ba782d9d7788978d2f754102c5633'
AIRTABLE_BASE_ID = 'app3gsLNAt0Mo7Nkm'
AIRTABLE_TABLE_NAME = 'User_IPs'

def add_record(username, ip_address):
    url = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'
    headers = {
        'Authorization': f'Bearer {AIRTABLE_API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'fields': {
            'Username': username,
            'IP Address': ip_address
        }
    
    }
    # print("types : ", type(username), type(ip_address))
    # print("feild: ", data)
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print(f"Record added to Airtable: {username} - {ip_address}")
    else:
        print(f"Failed to add record to Airtable: {response.text}")

# Add more functions as needed, like update_record, delete_record, etc.
