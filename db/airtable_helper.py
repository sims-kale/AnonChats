import random

import requests
import json
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
relative_path = os.path.join(current_dir, "../config", "dbconfig.json")

with open(relative_path) as f:
    config = json.load(f)

# delete_token = config["delete_token"]
write_token = config["write_token"]
read_token = config["read_token"]
AIRTABLE_BASE_ID = config["AIRTABLE_BASE_ID"]
AIRTABLE_TABLE_NAME = config["AIRTABLE_TABLE_NAME"]
AIRTABLE_PROFILE_TABLE_NAME = config["AIRTABLE_PROFILE_TABLE_NAME"]


def refresh_airtable():
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}"
    airtable_headers = {
        "Authorization": f"Bearer {read_token}",
        "Content-Type": "application/json"
    }
    airtable_response = requests.get(
        url, headers=airtable_headers)

    if airtable_response.status_code == 200:
        airtable_data = airtable_response.json()
        records = airtable_data.get("records", [])

        for record in records:
            record_id = record["id"]
            # Delete each record by ID
            delete_url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}/{record_id}"
            airtable_headers = {
                "Authorization": f"Bearer {write_token}",
                "Content-Type": "application/json"
            }
            delete_response = requests.delete(
                delete_url, headers=airtable_headers)

            if delete_response.status_code == 200:
                print(f"Deleted record with ID: {record_id}")
            else:
                print(
                    f"Failed to delete record with ID: {record_id}. Status code: {delete_response.status_code}")

    else:
        print(
            f"Failed to delete query Airtable. Status code: {airtable_response.status_code} {airtable_response.text}")


def getProfileUrl(username):
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_PROFILE_TABLE_NAME}"
    headers = {
        "Authorization": f"Bearer {read_token}",
        "Content-Type": "application/json",
    }
    params = {"filterByFormula": f"{{Username}} = '{username}'"}
    res = requests.get(url, headers=headers, params=params)
    try:
        if res.status_code == 200:
            data = res.json()
            records = data.get("records", [])
            if records:
                fields = records[0].get(
                    "fields", {}
                )
                random_number = random.choice([1, 2, 3])
                # Return the fields of the first matching record
                profile_image_url = fields.get("img_" + str(random_number))
                return profile_image_url
            else:
                return None
    except:
        print(f"Error in get records from airtable : {res.status_code}")


refresh_airtable()
#  Edit the Cron Jobs: Use the crontab -e command to edit the cron jobs.
# 0 0 * * * /path/to/python /path/to/airtable_helper.py      -CRONETAB Daily at 12.00am
