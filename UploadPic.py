"""
Function to upload image to filestack API
and save the url of the uploaded image
"""

import CommonVariables as cv


def img_upload(address):
    from filestack import Client
    key = Client("AlBPFPRHPSECAcbnonhuKz")
    filelnk = key.upload(filepath=address)
    print("Picture successfully uploaded!")
    cv.url = filelnk.url
    print(cv.url)
