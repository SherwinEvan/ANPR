# the main driver program
import CommonVariables
import UploadPic as up
import ALPR
import RegionCheck as rc
import OpenALPR
import SmartClickLPR

"""
Operation sequence : 
1) The local address of image is received and stored
2) ALPR() is run to check if plate is compatible region for OAPLR() and SCLPR()
3) UploadPic.img_upload() is run if plate is in compatible region
   + UploadPic.img_upload() uses filetack to generate image's url
   + OALPR(), and SCLPR() is run if region is defined for it
5) Result is displayed based on confidence level

Logic for confidence level calculation : 
- if all 3 APIs are used, most common result is displayed
- if only 2 APIs are used, result equality is checked and 
  difference in confidence level is checked
- if only 1 API is used, result is displayed directly
"""


def disp_data(plate_no, region, confidence1, confidence2):
    print("Number plate :", plate_no)
    print("Region :", region)
    print("Confidence level :", (confidence1 + confidence2) / 2)


while True:
    ALPR_data = None
    to_run = None
    address = None
    while True:
        try:
            address = input("Enter the local address of the picture : ")
            ALPR_data = ALPR.ALPR_detection(address)
            break
        except FileNotFoundError as FNFE:
            print("Enter a valid address!")

    if ALPR_data:
        to_run = rc.region(ALPR_data.detection_confidence, ALPR_data.region_code, ALPR_data.region_confidence)
    if to_run is None:
        print("No number plate detected.")
    elif to_run == 'ALPR':
        print("Plate detected!")
        disp_data(ALPR_data.plate_no, ALPR_data.region_code, ALPR_data.plate_confidence, ALPR_data.plate_confidence)
    else:
        print("Generating image url...")
        up.img_upload(address)
        OALPR_data = None
        SCLPR_data = None

        if to_run == 'SCLPR':
            OALPR_data = OpenALPR.OALPR('us', CommonVariables.url)
            SCLPR_data = SmartClickLPR.SCLPR(CommonVariables.url)

        elif to_run == 'OALPR':
            OALPR_data = OpenALPR.OALPR(ALPR_data.region_code, CommonVariables.url)

        if OALPR_data and SCLPR_data:
            if ALPR_data.plate_no == OALPR_data.plate_no:
                disp_data(ALPR_data.plate_no, ALPR_data.region_code, ALPR_data.plate_confidence,
                          OALPR_data.plate_confidence)

            elif ALPR_data.plate_no == SCLPR_data.plate_no:
                disp_data(ALPR_data.plate_no, 'us', ALPR_data.plate_confidence,
                          SCLPR_data.plate_confidence)

            elif OALPR_data.plate_no == SCLPR_data.plate_no:
                disp_data(OALPR_data.plate_no, 'us', OALPR_data.plate_confidence,
                          SCLPR_data.plate_confidence)

        elif OALPR_data:
            if OALPR_data.plate_no == ALPR_data.plate_no:
                disp_data(ALPR_data.plate_no, ALPR_data.region_code, ALPR_data.plate_confidence,
                          OALPR_data.plate_confidence)
            elif ALPR_data.plate_confidence > 0.5:
                disp_data(ALPR_data.plate_no, ALPR_data.region_code, OALPR_data.plate_confidence,
                          ALPR_data.plate_confidence)
            else:
                print("Both ALPR, and OALPR unable to recognise plate accurately.")
    while True:
        cont = input("Do you wish to recognise another plate (Y/N) : ")
        cont = cont.upper()
        if cont == 'N' or cont == 'NO' or \
                cont == 'Y' or cont == 'YES':
            break
        else:
            print("Enter a valid input.")

    if cont == 'N' or cont == 'NO':
        print("Terminating program.")
        break
