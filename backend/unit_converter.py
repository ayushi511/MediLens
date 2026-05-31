# Unit conversion factors to standard units
UNIT_CONVERSIONS = {
    "glucose": {
        "mmol/l": ("mg/dL", 18.0182),
        "mg/dl": ("mg/dL", 1.0),
    },
    "cholesterol": {
        "mmol/l": ("mg/dL", 38.665),
        "mg/dl": ("mg/dL", 1.0),
    },
    "hba1c": {
        "mmol/mol": ("%", 0.0915),  # IFCC to NGSP
        "%": ("%", 1.0),
    },
    "creatinine": {
        "umol/l": ("mg/dL", 0.01131),
        "mg/dl": ("mg/dL", 1.0),
    },
    "uric_acid": {
        "umol/l": ("mg/dL", 0.01681),
        "mg/dl": ("mg/dL", 1.0),
    },
    "vitamin_d": {
        "nmol/l": ("ng/mL", 0.4006),
        "ng/ml": ("ng/mL", 1.0),
    },
    "calcium": {
        "mmol/l": ("mg/dL", 4.0),
        "mg/dl": ("mg/dL", 1.0),
    },
    "sodium": {
        "mmol/l": ("mEq/L", 1.0),
        "meq/l": ("mEq/L", 1.0),
    },
    "potassium": {
        "mmol/l": ("mEq/L", 1.0),
        "meq/l": ("mEq/L", 1.0),
    },
    "bilirubin": {
        "umol/l": ("mg/dL", 0.05848),
        "mg/dl": ("mg/dL", 1.0),
    },
}

def convert_unit(test_name, value, detected_unit):
    """
    Convert value to standard unit for comparison.
    Returns (converted_value, standard_unit, was_converted)
    """
    test_conversions = UNIT_CONVERSIONS.get(test_name)
    if not test_conversions:
        return value, detected_unit, False

    unit_lower = detected_unit.lower().strip()
    conversion = test_conversions.get(unit_lower)

    if not conversion:
        return value, detected_unit, False

    standard_unit, factor = conversion
    converted = round(value * factor, 3)
    was_converted = factor != 1.0

    return converted, standard_unit, was_converted


def detect_unit(text_near_value):
    """
    Detect unit from text near the extracted value.
    """
    known_units = [
        "mg/dl", "mmol/l", "g/dl", "ng/ml", "nmol/l",
        "meq/l", "umol/l", "u/l", "iu/l", "10^3/ul",
        "million cells/ul", "miu/l", "%", "mmol/mol"
    ]
    text_lower = text_near_value.lower()
    for unit in known_units:
        if unit in text_lower:
            return unit
    return None