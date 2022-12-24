"""
Function to identify and return
plate number with OpenALPR
via RapidAPI

WORKS WITH US AND EU PLATES PRIMARILY
"""

import requests
import CommonVariables


# Function takes country of plate and image url to process
def OALPR(country, link):
    url = "https://openalpr.p.rapidapi.com/recognize_url"

    querystring = {"country": country}
    link.replace("/", "%2F")
    link.replace(":", "%3A")

    payload = "image_url="+link
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "****",
        "X-RapidAPI-Host": "openalpr.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    data = response.json()

    processed_data = None

    if data['results'] :
        processed_data = CommonVariables.OALPRData(data['results'][0]['plate'].upper(), data['results'][0]['confidence'])

    return processed_data

"""
Format of dictionary stored in data variable :
{"uuid": "", 
"data_type": "alpr_results", 
"epoch_time": 1669220005557, 
"processing_time": {"plates": 37.15127945, "total": 42.10099999909289}, 
"img_height": 768, 
"img_width": 1024, 
"results": [{"plate": "MH43C1745", "confidence": 94.9401474, "region_confidence": 66, 
    "vehicle_region": {"y": 43, "x": 122, "height": 529, "width": 683}, "region": "oh", 
    "plate_index": 0, "processing_time_ms": 5.59791422, 
    "candidates": [{"matches_template": 0, "plate": "MH43C1745", "confidence": 94.9401474}], 
    "coordinates": [{"y": 338, "x": 385}, {"y": 338, "x": 600}, {"y": 400, "x": 596}, {"y": 399, "x": 385}], 
    "matches_template": 0, "requested_topn": 10}], 
"credits_monthly_used": 73059, 
"version": 2, 
"credits_monthly_total": 100000000, 
"error": false, 
"regions_of_interest": [{"y": 0, "x": 0, "height": 768, "width": 1024}], 
"credit_cost": 1}
"""

"""
{'uuid': '', 
 'data_type': 'alpr_results', 
 'epoch_time': 1669310754238, 
 'processing_time': {'plates': 147.76338196, 'total': 296.1710000090534}, 
 'img_height': 432, 'img_width': 768, 
 'results': [], 
 'credits_monthly_used': 75505, 
 'version': 2, 
 'credits_monthly_total': 100000000, 
 'error': False, 
 'regions_of_interest': [{'y': 0, 'x': 0, 'height': 432, 'width': 768}], 
 'credit_cost': 1}
"""


