"""
Function to identify and return
plate number with ALPR

WORKS FOR MOST COUNTRIES

API is run and essential data is stored in object process_data of class ALPR
"""
import CommonVariables as cv
import requests


# Function takes local address fo image to process
def ALPR_detection(address):
    with open(address, 'rb') as fp:
        response = requests.post(
            'https://api.platerecognizer.com/v1/plate-reader/',
            files=dict(upload=fp),
            headers={'Authorization': 'Token ****'})
    all_data = response.json()

    processed_data = None
    if all_data['results']:
        processed_data = cv.ALPRData(all_data['results'][0]['plate'].upper(),
                                     all_data['results'][0]['region']['code'],
                                     all_data['results'][0]['region']['score'],
                                     all_data['results'][0]['dscore'],
                                     all_data['results'][0]['score'] * 100)
    return processed_data

"""
Format of dictionary stored in data variable :
{'processing_time': 32.45,
 'results': [{'box':
                  {'xmin': 105, 'ymin': 104, 'xmax': 199, 'ymax': 126},
              'plate': 'dl7cq1939', 'region': {'code': 'in', 'score': 0.84},
              'score': 0.896,
              'candidates': [{'score': 0.896, 'plate': 'dl7cq1939'},
                             {'score': 0.802, 'plate': 'dl7cqi939'}],
              'dscore': 0.861,
              'vehicle': {'score': 0.587, 'type': 'Sedan',
                          'box': {'xmin': 20, 'ymin': 8, 'xmax': 279, 'ymax': 173}}}],
 'filename': '1801_jekOl_creta_number_plate.jpg', 'version': 1, 'camera_id': None,
 'timestamp': '2022-11-22T18:01:44.386511Z'}
 """

"""
For invalid input :
{'processing_time': 43.628, 
'results': [], 
'filename': '1714_R43cw_HD-wallpaper-meteor-shower-forest-river-meteor-show-night.jpg', 
'version': 1, 
'camera_id': None, 
'timestamp': '2022-11-26T17:14:53.119531Z'}

"""
