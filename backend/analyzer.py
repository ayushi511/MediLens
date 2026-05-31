import re
from rules import NORMAL_RANGES, DEMOGRAPHIC_RANGES, get_age_bracket
from lab_range_extractor import extract_lab_ranges


def detect_unit(text):
    known_units = [
        "mg/dl", "mmol/l", "g/dl", "ng/ml", "nmol/l",
        "meq/l", "umol/l", "u/l", "iu/l", "10^3/ul",
        "million cells/ul", "miu/l", "%", "mmol/mol"
    ]
    text_lower = text.lower()
    for unit in known_units:
        if unit in text_lower:
            return unit
    return None


def convert_unit(test_name, value, detected_unit):
    CONVERSIONS = {
        "glucose":     {"mmol/l": ("mg/dL", 18.0182), "mg/dl": ("mg/dL", 1.0)},
        "cholesterol": {"mmol/l": ("mg/dL", 38.665),  "mg/dl": ("mg/dL", 1.0)},
        "creatinine":  {"umol/l": ("mg/dL", 0.01131), "mg/dl": ("mg/dL", 1.0)},
        "vitamin_d":   {"nmol/l": ("ng/mL", 0.4006),  "ng/ml": ("ng/mL", 1.0)},
        "calcium":     {"mmol/l": ("mg/dL", 4.0),     "mg/dl": ("mg/dL", 1.0)},
        "bilirubin":   {"umol/l": ("mg/dL", 0.05848), "mg/dl": ("mg/dL", 1.0)},
        "uric_acid":   {"umol/l": ("mg/dL", 0.01681), "mg/dl": ("mg/dL", 1.0)},
        "sodium":      {"mmol/l": ("mEq/L", 1.0),     "meq/l": ("mEq/L", 1.0)},
        "potassium":   {"mmol/l": ("mEq/L", 1.0),     "meq/l": ("mEq/L", 1.0)},
    }
    test_conv = CONVERSIONS.get(test_name)
    if not test_conv:
        return value, detected_unit, False
    unit_lower = detected_unit.lower().strip()
    conv = test_conv.get(unit_lower)
    if not conv:
        return value, detected_unit, False
    standard_unit, factor = conv
    return round(value * factor, 3), standard_unit, factor != 1.0


def normalize_value(test_name, value, raw_text_near):
    raw = raw_text_near.lower() if raw_text_near else ""
    if test_name == "platelets":
        if "lakh" in raw or "lac" in raw:
            return round(value * 100, 1)
    if test_name == "wbc":
        if "/c.mm" in raw or "/cumm" in raw or "cumm" in raw:
            if value > 1000:
                return round(value / 1000, 2)
    return value


def get_range_for_user(test_name, age, gender, pregnant, lab_ranges={}):
    if test_name in lab_ranges:
        r = lab_ranges[test_name]
        return r["min"], r["max"], "lab-provided range"
    bracket = get_age_bracket(age, gender, pregnant)
    if test_name in DEMOGRAPHIC_RANGES:
        demo = DEMOGRAPHIC_RANGES[test_name]
        range_data = demo.get(bracket) or demo.get("adult_male")
        if range_data:
            return range_data["min"], range_data["max"], bracket.replace("_", " ")
    rule = NORMAL_RANGES.get(test_name, {})
    return rule.get("min", 0), rule.get("max", 999), "default"



def find_value(text_lower, aliases):
    lines = text_lower.split('\n')

    for alias in aliases:
        for i, line in enumerate(lines):
            if alias not in line:
                continue

            search_block = lines[i:i+4]

            for search_line in search_block:
                # Skip reference range lines
                if re.search(r'\d+\s*[-–]\s*\d+', search_line):
                    continue
                if re.search(r'<\s*\d+', search_line):
                    continue
                if re.search(r'>\s*\d+', search_line):
                    continue

                # Skip non-result lines
                skip_words = ['reference', 'range', 'interval', 'normal',
                              'deficiency', 'insufficiency', 'sufficiency',
                              'interpretation', 'caution', 'page', 'report']
                if any(word in search_line for word in skip_words):
                    continue

                numbers = re.findall(r'\b(\d+\.?\d*)\b', search_line)
                for num_str in numbers:
                    candidate = float(num_str)
                    if candidate < 0.01 or candidate > 9999:
                        continue
                    if 2000 <= candidate <= 2099:
                        continue

                    raw_after = search_line[search_line.find(num_str)+len(num_str):][:30]
                    return candidate, raw_after

    return None, None

def extract_and_analyze(text, age=30, gender="male", pregnant=False):
    results = []
    text_lower = text.lower()

    lab_ranges = extract_lab_ranges(text)

    SYNONYMS = {
        "hemoglobin":  ["haemoglobin", "hemoglobin", "hb ", "hgb",
                        "haemogram\nhb", "haemogram hb"],
        "rbc":         ["rbc", "red blood cell", "red blood cells", "erythrocytes"],
        "wbc":         ["total w.b.c.count", "total w.b.c", "total wbc",
                        "wbc", "white blood cell", "leukocytes", "tlc", "w.b.c"],
        "platelets":   ["platelets", "platelet count", "plt", "thrombocytes"],
        "glucose":     ["blood sugar fasting", "glucose (fasting)",
                        "glucose", "blood sugar", "fasting glucose", "fbs", "rbs"],
        "hba1c":       ["hba1c (glycosylated hb)", "hba1c(glycosylated hb)",
                        "glycosylated hb", "hba1c", "glycated hemoglobin", "a1c"],
        "cholesterol": ["total cholesterol", "cholesterol", "serum cholesterol"],
        "creatinine":  ["creatinine", "serum creatinine", "s. creatinine"],
        "tsh":         ["tsh", "thyroid stimulating hormone", "thyrotropin"],
        "uric_acid":   ["uric acid", "serum uric acid", "s. uric acid"],
        "sodium":      ["sodium", "serum sodium", "na+"],
        "potassium":   ["potassium", "serum potassium", "k+"],
        "bilirubin":   ["total bilirubin", "serum bilirubin", "bilirubin"],
        "sgpt":        ["sgpt", "alt", "alanine aminotransferase"],
        "sgot":        ["sgot", "ast", "aspartate aminotransferase"],
        "vitamin_d":   ["vitamin d total - 25 hydroxy", "vitamin d total",
                        "vitamin d", "vit d", "25-oh vitamin d",
                        "vitamin d3", "25 hydroxy", "hydroxy (oh)"],
        "calcium":     ["calcium", "serum calcium", "ca++"],
        "vitamin_b12": ["vitamin b12 (cya", "vitamin b12 (cyanocobalamin)",
                        "vitamin b12", "cyanocobalamin", "vit b12",
                        "vitamin b 12", "b12"],
    }

    extracted_values = []

    for test_name, rule in NORMAL_RANGES.items():
        aliases = SYNONYMS.get(test_name, [test_name.replace("_", " ")])

        value, raw_match_text = find_value(text_lower, aliases)

        if value is None:
            continue

        value = normalize_value(test_name, value, raw_match_text)

        detected_unit = detect_unit(raw_match_text or "")
        was_converted = False
        original_value = value
        original_unit = detected_unit

        if detected_unit:
            value, detected_unit, was_converted = convert_unit(
                test_name, value, detected_unit
            )

        extracted_values.append({
            "test":            test_name.replace("_", " ").capitalize(),
            "value":           original_value,
            "unit":            original_unit or rule["unit"],
            "converted_value": value if was_converted else None,
            "converted_unit":  detected_unit if was_converted else None,
            "was_converted":   was_converted,
        })

        min_val, max_val, range_source = get_range_for_user(
            test_name, age, gender, pregnant, lab_ranges
        )

        critical_low  = rule.get("critical_low")
        critical_high = rule.get("critical_high")

        if critical_low and value <= critical_low:
            status   = "CRITICAL LOW"
            message  = f"🚨 {rule['low_msg']}"
            severity = "critical"
        elif critical_high and value >= critical_high:
            status   = "CRITICAL HIGH"
            message  = f"🚨 {rule['high_msg']}"
            severity = "critical"
        elif value < min_val:
            status   = "LOW"
            message  = rule["low_msg"]
            severity = rule.get("severity_low", "moderate")
        elif value > max_val:
            status   = "HIGH"
            message  = rule["high_msg"]
            severity = rule.get("severity_high", "moderate")
        else:
            status   = "NORMAL"
            message  = rule["normal_msg"]
            severity = "low"

        if status != "NORMAL":
            if value < min_val:
                pct_off   = round(((min_val - value) / min_val) * 100, 1)
                deviation = f"{pct_off}% below minimum"
            else:
                pct_off   = round(((value - max_val) / max_val) * 100, 1)
                deviation = f"{pct_off}% above maximum"
        else:
            deviation = "Within normal range"

        results.append({
            "test":           test_name.replace("_", " ").capitalize(),
            "value":          value,
            "unit":           rule["unit"],
            "status":         status,
            "message":        message,
            "emoji":          rule.get("emoji", "🧪"),
            "severity":       severity,
            "normal_range":   f"{min_val} - {max_val} {rule['unit']}",
            "range_source":   range_source,
            "deviation":      deviation,
            "unit_converted": was_converted,
            "original_value": original_value if was_converted else None,
            "original_unit":  original_unit  if was_converted else None,
            "what_it_means":  rule.get(
                "what_it_means_high" if "HIGH" in status
                else "what_it_means_low", []
            ),
            "eat":                rule.get("eat", []),
            "avoid":              rule.get("avoid", []),
            "tips":               rule.get("tips", []),
            "see_doctor_if":      rule.get("see_doctor_if", []),
            "related_tests":      rule.get("related_tests", []),
            "did_you_know":       rule.get("did_you_know", ""),
            "category":           rule.get("category", ""),
            "medical_disclaimer": rule.get("medical_disclaimer", ""),
        })

    return results, extracted_values