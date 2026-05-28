import re
from rules import NORMAL_RANGES

def extract_and_analyze(text):
    results = []
    text_lower = text.lower()

    for test_name, rule in NORMAL_RANGES.items():
        pattern = rf"{test_name.replace('_', ' ')}[\s:]*([0-9]+\.?[0-9]*)"
        match = re.search(pattern, text_lower)

        if match:
            value = float(match.group(1))
            min_val = rule["min"]
            max_val = rule["max"]
            critical_low = rule.get("critical_low", None)
            critical_high = rule.get("critical_high", None)

            # Determine status
            if critical_low and value <= critical_low:
                status = "CRITICAL LOW"
                message = f"🚨 URGENT: {rule['low_msg']}"
                emoji = "🚨"
                severity = "critical"
            elif critical_high and value >= critical_high:
                status = "CRITICAL HIGH"
                message = f"🚨 URGENT: {rule['high_msg']}"
                emoji = "🚨"
                severity = "critical"
            elif value < min_val:
                status = "LOW"
                message = rule["low_msg"]
                emoji = "⬇️"
                severity = rule.get("severity_low", "moderate")
            elif value > max_val:
                status = "HIGH"
                message = rule["high_msg"]
                emoji = "⬆️"
                severity = rule.get("severity_high", "moderate")
            else:
                status = "NORMAL"
                message = rule["normal_msg"]
                emoji = "✅"
                severity = "low"

            results.append({
                "test": test_name.replace("_", " ").capitalize(),
                "value": value,
                "unit": rule["unit"],
                "status": status,
                "message": message,
                "emoji": emoji,
                "severity": severity,
                "normal_range": f"{min_val} - {max_val} {rule['unit']}",
                "what_it_means": rule.get("what_it_means_high" if "HIGH" in status else "what_it_means_low", []),
                "eat": rule.get("eat", []),
                "avoid": rule.get("avoid", []),
                "tips": rule.get("tips", []),
                "see_doctor_if": rule.get("see_doctor_if", []),
                "related_tests": rule.get("related_tests", []),
                "did_you_know": rule.get("did_you_know", ""),
                "category": rule.get("category", ""),
                "medical_disclaimer": rule.get("medical_disclaimer", ""),
            })

    return results