# A file to store globally used data

# Data classes are used as structures to store essential data
class ALPRData:
    def __init__(self, plate_no, region_code, region_confidence, detection_confidence, plate_confidence):
        self.plate_no = plate_no
        self.region_code = region_code
        self.region_confidence = region_confidence
        self.detection_confidence = detection_confidence
        self.plate_confidence = plate_confidence


class OALPRData:
    def __init__(self, plate_no, plate_confidence):
        self.plate_no = plate_no
        self.plate_confidence = plate_confidence


class SCLPRData:
    def __init__(self, plate_no, plate_confidence):
        self.plate_no = plate_no
        self.plate_confidence = plate_confidence


address = None
url = None
