import requests


import json

with open("../config/dbconfig.json") as f:
    config = json.load(f)

write_token = config["write_token"]
read_token = config["read_token"]
AIRTABLE_BASE_ID = config["AIRTABLE_BASE_ID"]
AIRTABLE_TABLE_NAME = config["AIRTABLE_TABLE_NAME"]


def add_record(nickname, ip_address):
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}"
    headers = {
        "Authorization": f"Bearer {write_token}",
        "Content-Type": "application/json",
    }
    data = {"fields": {"Username": nickname, "IP Address": ip_address}}

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print(f"Record added to Airtable: {nickname} - {ip_address}")
    else:
        print(f"Failed to add record to Airtable: {response.text}")


def matchUsername(ip_address):
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}"
    headers = {
        "Authorization": f"Bearer {read_token}",
        "Content-Type": "application/json",
    }
    params = {"filterByFormula": f"{{IP Address}} = '{ip_address}'"}
    res = requests.get(url, headers=headers, params=params)
    try:
        if res.status_code == 200:
            data = res.json()
            records = data.get("records", [])
            if records:
                fields = records[0].get(
                    "fields", {}
                )  # Return the fields of the first matching record
                matched_username = fields.get("Username")
                return matched_username
            else:
                return None
    except:
        print(f"Error in get records from airtable : {res.status_code}")

def UserExists(nickname):
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}"
    headers = {
        "Authorization": f"Bearer {read_token}",
        "Content-Type": "application/json",
    }
    params = {"filterByFormula": f"{{Username}} = '{nickname}'"}
    res = requests.get(url, headers=headers, params=params)
    try:
        if res.status_code == 200:
            data = res.json()
            records = data.get("records", [])
            if records:
                return True
            else:
                return False
    except:
        print(f"Error in get records from airtable : {res.status_code}")

# UserExists(nickname='BOO')