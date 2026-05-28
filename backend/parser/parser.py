import re

NORMAL_RANGES = {
    "Hemoglobin": (12, 14),
    "RBC": (3.8, 5.5),
    "WBC": (4000, 10000),
    "Platelets": (1.5, 4.0)
}

def get_status(test, value):

    low, high = NORMAL_RANGES[test]

    value = float(value)

    if value < low:
        return "Low"

    elif value > high:
        return "High"

    return "Normal"


def extract_tests(text):

    patterns = {
        "Hemoglobin": r"HAEMOGLOBIN\s+([\d.]+)",
        "RBC": r"RBC\s+([\d.]+)",
        "WBC": r"Total W\.B\.C\.Count\s+(\d+)",
        "Platelets": r"PLATELETS\s+([\d.]+)"
    }

    results = []

    for test, pattern in patterns.items():

        match = re.search(pattern, text)

        if match:

            value = match.group(1)

            results.append({
                "test": test,
                "value": value,
                "status": get_status(test, value)
            })

    return results