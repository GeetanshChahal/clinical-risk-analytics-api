def calculate_risk(vitals):
    score = 0

    for v in vitals:
        if v["heart_rate"] > 110:
            score += 2
        if v["oxygen"] < 92:
            score += 3
        if v["temperature"] > 38:
            score += 2
        if v["bp_sys"] > 140:
            score += 1

    avg_score = score / len(vitals) if vitals else 0

    if avg_score > 2:
        level = "High"
    elif avg_score > 1:
        level = "Medium"
    else:
        level = "Low"

    return {"risk_score": avg_score, "risk_level": level}