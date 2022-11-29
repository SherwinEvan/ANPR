# File to check if OAPLR and SCLPR is worth calling


def region(detection_confidence, region_code, region_confidence):
    if detection_confidence < 0.5:
        return None

    if region_code.startswith('us'):
        return 'SCLPR'

    if region_code.startswith('br'):
        return 'OALPR'

    OALPR_regions = ['eu', 'fr', 'gb', 'in', 'kr', 'mx', 'sg', 'vn']

    if region_code in OALPR_regions:
        return 'OALPR'

    elif region_confidence < 0.5:
        return None

    return 'ALPR'
