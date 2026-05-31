import re

def extract_lab_ranges(text):
    """
    Try to extract lab-provided reference ranges from the PDF text.
    Returns dict: { "hemoglobin": (min, max), ... }
    """
    lab_ranges = {}

    # Common patterns labs use for reference ranges
    patterns = [
        # Pattern: "13.5 - 17.5" or "13.5-17.5"
        r'(\d+\.?\d*)\s*[-–to]+\s*(\d+\.?\d*)',
        # Pattern: "Normal: 13.5 - 17.5"
        r'(?:normal|reference|ref\.?|range)\s*:?\s*(\d+\.?\d*)\s*[-–]\s*(\d+\.?\d*)',
    ]

    # Test name synonyms to match
    SYNONYMS = {
        "hemoglobin": ["hemoglobin", "haemoglobin", "hb", "hgb"],
        "glucose":    ["glucose", "blood sugar", "fbs", "rbs"],
        "cholesterol":["cholesterol", "total cholesterol"],
        "creatinine": ["creatinine", "serum creatinine"],
        "tsh":        ["tsh", "thyroid stimulating"],
        "wbc":        ["wbc", "white blood cell", "tlc"],
        "platelets":  ["platelets", "plt"],
        "sgpt":       ["sgpt", "alt"],
        "sgot":       ["sgot", "ast"],
        "bilirubin":  ["bilirubin", "total bilirubin"],
        "vitamin_d":  ["vitamin d", "vit d", "25-oh"],
        "calcium":    ["calcium"],
        "sodium":     ["sodium"],
        "potassium":  ["potassium"],
        "uric_acid":  ["uric acid"],
        "hba1c":      ["hba1c", "a1c"],
    }

    lines = text.lower().split('\n')

    for line in lines:
        for test_name, aliases in SYNONYMS.items():
            for alias in aliases:
                if alias in line:
                    # Try to find reference range on same line
                    for pattern in patterns:
                        match = re.search(pattern, line)
                        if match:
                            try:
                                min_val = float(match.group(1))
                                max_val = float(match.group(2))
                                if min_val < max_val and min_val >= 0:
                                    lab_ranges[test_name] = {
                                        "min": min_val,
                                        "max": max_val,
                                        "source": "lab_provided"
                                    }
                            except:
                                pass
                    break

    return lab_ranges