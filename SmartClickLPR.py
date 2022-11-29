"""
Function to identify and return
plate number with SmartClick
via RapidAPI

WORKS ONLY FOR AMERICAN PLATES
"""

import requests
import CommonVariables


# Function takes image url to process
def SCLPR(link):
    url = "https://license-plate-detection.p.rapidapi.com/license-plate-detection"

    payload = {
        "url": link}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "efd8db2574mshc552705d758633ap12ba03jsnf72704c92b15",
        "X-RapidAPI-Host": "license-plate-detection.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    data = response.json()

    processed_data = CommonVariables.SCLPRData(data[0]['value'].upper(), data[0]['confidence'] * 100)

    return processed_data


"""
Format of dictionary stored in data variable :
[{"label":"License_Plate","coordinate":[380.0,440.0,681.0,506.0],"confidence":0.7663224935531616,"value":"RL4003"}]
"""
