# Age bracket helper
def get_age_bracket(age, gender, pregnant=False):
    if pregnant and gender == "female":
        return "pregnant"
    if age < 13:
        return "child"
    if age < 18:
        return "teen"
    if age >= 60:
        return "senior"
    return f"adult_{gender}" if gender in ["male", "female"] else "adult_male"

# Demographic-aware ranges
DEMOGRAPHIC_RANGES = {
    "hemoglobin": {
        "adult_male":   {"min": 13.5, "max": 17.5},
        "adult_female": {"min": 12.0, "max": 15.5},
        "child":        {"min": 11.0, "max": 14.0},
        "teen":         {"min": 12.0, "max": 16.0},
        "senior":       {"min": 11.5, "max": 16.5},
        "pregnant":     {"min": 11.0, "max": 14.0},
    },
    "rbc": {
        "adult_male":   {"min": 4.7, "max": 6.1},
        "adult_female": {"min": 4.2, "max": 5.4},
        "child":        {"min": 4.0, "max": 5.5},
        "teen":         {"min": 4.2, "max": 5.8},
        "senior":       {"min": 4.0, "max": 5.5},
        "pregnant":     {"min": 3.8, "max": 5.2},
    },
    "wbc": {
        "adult_male":   {"min": 4.5, "max": 11.0},
        "adult_female": {"min": 4.5, "max": 11.0},
        "child":        {"min": 5.0, "max": 15.0},
        "teen":         {"min": 4.5, "max": 13.0},
        "senior":       {"min": 4.0, "max": 10.5},
        "pregnant":     {"min": 6.0, "max": 16.0},
    },
    "platelets": {
        "adult_male":   {"min": 150, "max": 400},
        "adult_female": {"min": 150, "max": 400},
        "child":        {"min": 150, "max": 450},
        "teen":         {"min": 150, "max": 400},
        "senior":       {"min": 150, "max": 380},
        "pregnant":     {"min": 100, "max": 400},
    },
    "glucose": {
        "adult_male":   {"min": 70, "max": 100},
        "adult_female": {"min": 70, "max": 100},
        "child":        {"min": 60, "max": 100},
        "teen":         {"min": 70, "max": 100},
        "senior":       {"min": 80, "max": 110},
        "pregnant":     {"min": 65, "max": 92},
    },
    "creatinine": {
        "adult_male":   {"min": 0.7, "max": 1.3},
        "adult_female": {"min": 0.5, "max": 1.1},
        "child":        {"min": 0.3, "max": 0.7},
        "teen":         {"min": 0.5, "max": 1.0},
        "senior":       {"min": 0.6, "max": 1.2},
        "pregnant":     {"min": 0.4, "max": 0.8},
    },
    "tsh": {
        "adult_male":   {"min": 0.4, "max": 4.0},
        "adult_female": {"min": 0.4, "max": 4.0},
        "child":        {"min": 0.7, "max": 5.7},
        "teen":         {"min": 0.5, "max": 4.5},
        "senior":       {"min": 0.5, "max": 5.0},
        "pregnant":     {"min": 0.1, "max": 2.5},
    },
}
NORMAL_RANGES = {

    "hemoglobin": {
        "min": 13.5,
        "max": 17.5,
        "critical_low": 7.0,
        "critical_high": 20.0,
        "unit": "g/dL",
        "severity_low": "moderate",
        "severity_high": "moderate",
        "low_msg":
            "Your hemoglobin level is below the normal reference range. "
            "Hemoglobin is responsible for carrying oxygen from the lungs to the body's tissues. "
            "Low hemoglobin levels may suggest anemia, iron deficiency, blood loss, nutritional deficiency, "
            "or certain chronic medical conditions. "
            "Common symptoms may include tiredness, weakness, dizziness, shortness of breath, pale skin, "
            "or reduced physical stamina.",
        "high_msg":
            "Your hemoglobin level is above the normal reference range. "
            "This may occur due to dehydration, smoking, chronic lung conditions, living at high altitudes, "
            "or certain blood-related disorders. "
            "Persistently elevated hemoglobin levels can sometimes increase blood thickness and may require medical evaluation.",
        "normal_msg":
            "Your hemoglobin level falls within the normal range. "
            "This suggests that your blood is likely carrying oxygen efficiently throughout the body.",
        "what_it_means_low": [
            "Low hemoglobin may reduce oxygen delivery to tissues and organs",
            "Iron deficiency anemia is one of the most common causes",
            "May occur due to poor diet, blood loss, or vitamin deficiencies",
            "Can lead to fatigue, weakness, dizziness, or headaches"
        ],
        "what_it_means_high": [
            "May occur due to dehydration or smoking",
            "Can be seen in people living at high altitude",
            "Sometimes associated with lung or blood disorders",
            "Very high levels may increase risk of blood clotting"
        ],
        "eat": [
            "Spinach and green leafy vegetables",
            "Beetroot and pomegranate",
            "Iron-rich cereals and legumes",
            "Eggs and lean meat",
            "Vitamin C rich foods such as oranges, amla, and lemons"
        ],
        "avoid": [
            "Tea or coffee immediately after meals as they inhibit iron absorption",
            "Highly processed junk foods low in nutritional value",
            "Skipping meals frequently",
            "Excess alcohol intake"
        ],
        "tips": [
            "Combine iron-rich foods with Vitamin C sources for better absorption",
            "Maintain adequate hydration throughout the day",
            "Ensure proper sleep and a balanced, nutrient-rich diet",
            "Take iron or vitamin supplements only if prescribed by a healthcare professional"
        ],
        "see_doctor_if": [
            "You experience severe fatigue or breathlessness with minimal exertion",
            "You notice chest pain or episodes of fainting",
            "Your hemoglobin remains abnormal on repeated testing",
            "You experience rapid heartbeat or severe unexplained weakness"
        ],
        "related_tests": ["rbc", "wbc", "platelets"],
        "did_you_know":
            "Hemoglobin is the iron-containing protein inside red blood cells that helps transport oxygen throughout the body.",
        "category": "Blood Test",
        "emoji": "🩸",
        "medical_disclaimer":
            "This AI-generated interpretation is intended for informational and educational purposes only. "
            "Laboratory values should always be interpreted by a qualified healthcare professional in combination "
            "with symptoms, medical history, medications, and clinical examination."
    },

    "rbc": {
        "min": 4.7,
        "max": 6.1,
        "critical_low": 3.0,
        "critical_high": 7.5,
        "unit": "million cells/uL",
        "severity_low": "moderate",
        "severity_high": "moderate",
        "low_msg":
            "Your red blood cell (RBC) count is below the normal reference range. "
            "Red blood cells are responsible for transporting oxygen from the lungs to every part of the body "
            "and returning carbon dioxide back for exhalation. "
            "A low RBC count may indicate anemia, nutritional deficiencies such as iron, folate, or Vitamin B12, "
            "blood loss, bone marrow disorders, or certain chronic diseases. "
            "Symptoms can include persistent fatigue, pallor, shortness of breath, and reduced exercise tolerance.",
        "high_msg":
            "Your red blood cell count is higher than the normal reference range. "
            "An elevated RBC count may be seen in conditions such as dehydration, chronic low oxygen states "
            "such as lung disease or high-altitude living, smoking, or in rare blood disorders. "
            "Increased RBC count can thicken the blood, potentially raising the risk of clot formation.",
        "normal_msg":
            "Your red blood cell count is within the normal range. "
            "This indicates that your body is likely producing and maintaining an adequate number of red blood cells "
            "to support normal oxygen transport.",
        "what_it_means_low": [
            "May indicate iron deficiency anemia or nutritional anemia",
            "Can result from chronic blood loss such as heavy menstruation or gastrointestinal bleeding",
            "Reduced oxygen supply may lead to fatigue, pallor, and weakness",
            "May also occur in bone marrow suppression or chronic kidney disease"
        ],
        "what_it_means_high": [
            "Can occur with dehydration, reducing plasma volume and concentrating RBCs",
            "May be linked to chronic hypoxia from lung disease or smoking",
            "Polycythemia vera, a rare bone marrow condition, can also cause elevated RBC",
            "Elevated RBC may increase the risk of blood clots"
        ],
        "eat": [
            "Iron-rich foods such as lentils, beans, and dark leafy greens",
            "Vitamin B12 sources such as eggs, dairy, and lean meats",
            "Folate-rich foods such as spinach, chickpeas, and fortified cereals",
            "Protein-rich foods to support red blood cell production"
        ],
        "avoid": [
            "Smoking, which can artificially elevate RBC counts",
            "Excess consumption of junk or processed foods with poor nutritional value",
            "Alcohol, which can interfere with red blood cell production"
        ],
        "tips": [
            "Maintain a well-balanced diet rich in iron, B12, and folate",
            "Stay well hydrated to avoid false concentration of blood cells",
            "Get regular blood tests if you are at risk for anemia or blood disorders",
            "Report any unusual fatigue, paleness, or breathlessness to your doctor"
        ],
        "see_doctor_if": [
            "You experience severe or persistent fatigue and weakness",
            "You notice chest pain, palpitations, or shortness of breath",
            "Your RBC count is significantly outside the normal range on repeated testing",
            "You suspect chronic blood loss or have a known blood disorder"
        ],
        "related_tests": ["hemoglobin", "wbc", "platelets"],
        "did_you_know":
            "A single drop of blood contains approximately 5 million red blood cells, each living for about 120 days before being recycled by the body.",
        "category": "Blood Test",
        "emoji": "🔴",
        "medical_disclaimer":
            "This AI-generated interpretation is intended for informational and educational purposes only. "
            "Laboratory values should always be interpreted by a qualified healthcare professional in combination "
            "with symptoms, medical history, medications, and clinical examination."
    },

    "wbc": {
        "min": 4.5,
        "max": 11.0,
        "critical_low": 2.0,
        "critical_high": 30.0,
        "unit": "10^3/uL",
        "severity_low": "moderate",
        "severity_high": "moderate",
        "low_msg":
            "Your white blood cell (WBC) count is below the normal reference range. "
            "White blood cells are the primary defenders of your immune system, protecting the body "
            "against infections, bacteria, viruses, and other foreign substances. "
            "A low WBC count, also known as leukopenia, may be caused by viral infections, bone marrow suppression, "
            "autoimmune conditions, nutritional deficiencies, or certain medications such as chemotherapy. "
            "This may leave you more vulnerable to infections and illnesses.",
        "high_msg":
            "Your white blood cell count is above the normal reference range. "
            "An elevated WBC count, known as leukocytosis, is commonly seen during active infections, "
            "inflammatory conditions, allergic reactions, physical stress, or in response to certain medications. "
            "In rare cases, persistently very high WBC levels may require further evaluation to rule out blood-related disorders.",
        "normal_msg":
            "Your white blood cell count is within the normal range. "
            "This suggests that your immune system is functioning within expected parameters "
            "and is adequately equipped to defend the body against common infections.",
        "what_it_means_low": [
            "Leukopenia can significantly weaken immune defenses against infections",
            "May result from viral illnesses, bone marrow dysfunction, or certain medications",
            "Nutritional deficiencies such as folate and Vitamin B12 can reduce WBC production",
            "Low WBC may increase susceptibility to bacterial and fungal infections"
        ],
        "what_it_means_high": [
            "Often indicates the body is fighting an active bacterial or viral infection",
            "Can also occur during inflammatory conditions or allergic reactions",
            "Physical or emotional stress can transiently raise WBC counts",
            "Persistent unexplained elevation should be evaluated to rule out blood cancers"
        ],
        "eat": [
            "Citrus fruits rich in Vitamin C such as oranges, kiwi, and guava",
            "Garlic and ginger, which have natural immune-supportive properties",
            "Yogurt and probiotic-rich fermented foods",
            "Dark leafy vegetables such as spinach and kale",
            "Zinc-rich foods such as pumpkin seeds, nuts, and legumes"
        ],
        "avoid": [
            "Smoking and tobacco products that impair immune function",
            "Excess alcohol, which can suppress bone marrow activity",
            "Highly processed foods low in micronutrients",
            "Unnecessary antibiotics without medical supervision"
        ],
        "tips": [
            "Prioritize adequate and restful sleep to support immune function",
            "Manage chronic stress through relaxation techniques or physical activity",
            "Practice good hand hygiene to reduce infection risk, especially with low WBC",
            "Report any recurrent infections, fever, or unusual fatigue to your doctor"
        ],
        "see_doctor_if": [
            "You experience persistent or recurrent fever and infections",
            "You are on medications known to affect white blood cell counts",
            "Your WBC count is critically low or persistently high on repeated tests",
            "You develop unexplained fatigue, night sweats, or swollen lymph nodes"
        ],
        "related_tests": ["hemoglobin", "platelets", "rbc"],
        "did_you_know":
            "There are five main types of white blood cells, each with a unique role in your immune defense system, including neutrophils, lymphocytes, monocytes, eosinophils, and basophils.",
        "category": "Immunity",
        "emoji": "🛡️",
        "medical_disclaimer":
            "This AI-generated interpretation is intended for informational and educational purposes only. "
            "Laboratory values should always be interpreted by a qualified healthcare professional in combination "
            "with symptoms, medical history, medications, and clinical examination."
    },

    "platelets": {
        "min": 150,
        "max": 400,
        "critical_low": 50,
        "critical_high": 1000,
        "unit": "10^3/uL",
        "severity_low": "high",
        "severity_high": "moderate",
        "low_msg":
            "Your platelet count is below the normal reference range. "
            "Platelets are small blood cells that play a critical role in forming blood clots to stop bleeding "
            "after an injury. A low platelet count, known as thrombocytopenia, can increase your risk of "
            "prolonged bleeding, easy bruising, or spontaneous bleeding in severe cases. "
            "Common causes include viral infections such as dengue, immune disorders, nutritional deficiencies, "
            "certain medications, or bone marrow conditions.",
        "high_msg":
            "Your platelet count is above the normal reference range. "
            "A mildly elevated platelet count, known as thrombocytosis, may occur as a reactive response "
            "to infection, inflammation, iron deficiency anemia, or physical stress. "
            "In some cases, persistently high platelet counts may require further evaluation, "
            "as they can theoretically increase the risk of clot formation.",
        "normal_msg":
            "Your platelet count is within the normal range. "
            "This indicates that your blood clotting mechanism is likely functioning adequately, "
            "helping your body manage minor bleeding and injuries effectively.",
        "what_it_means_low": [
            "Increases the risk of prolonged bleeding even from minor cuts or injuries",
            "Can cause spontaneous bruising, nosebleeds, or bleeding gums",
            "Dengue fever, autoimmune diseases, and certain medications are common causes",
            "Severe thrombocytopenia may require urgent medical attention"
        ],
        "what_it_means_high": [
            "Reactive thrombocytosis often occurs with infection, inflammation, or iron deficiency",
            "May increase the theoretical risk of blood clot formation in some individuals",
            "Persistent or markedly elevated counts should be evaluated for underlying causes",
            "Usually not dangerous when it occurs as a temporary reactive response"
        ],
        "eat": [
            "Papaya and papaya leaf extract, traditionally associated with platelet support",
            "Pomegranate and other antioxidant-rich fruits",
            "Vitamin B12 sources such as eggs and dairy products",
            "Folate-rich foods such as spinach and legumes",
            "Vitamin K-containing leafy greens for healthy clotting function"
        ],
        "avoid": [
            "Alcohol, which can suppress platelet production in the bone marrow",
            "Smoking, which can impair overall blood cell health",
            "Aspirin and NSAIDs unless specifically prescribed, as they affect platelet function",
            "High-risk activities when platelet count is critically low"
        ],
        "tips": [
            "Monitor for unusual bruising, prolonged bleeding, or petechiae (tiny red skin spots)",
            "Inform your doctor about all medications you are taking",
            "Avoid contact sports or injury-prone activities if your count is significantly low",
            "Repeat blood tests as advised to track trends over time"
        ],
        "see_doctor_if": [
            "You notice bleeding gums, frequent nosebleeds, or blood in urine or stools",
            "Bruises appear without any obvious injury",
            "Your platelet count falls into the critically low range",
            "You develop a rash of tiny red or purple spots on your skin"
        ],
        "related_tests": ["wbc", "hemoglobin", "rbc"],
        "did_you_know":
            "Platelets are the smallest blood cells and have a very short lifespan of only about 7 to 10 days, after which they are replaced by new ones produced in the bone marrow.",
        "category": "Blood Test",
        "emoji": "🩹",
        "medical_disclaimer":
            "This AI-generated interpretation is intended for informational and educational purposes only. "
            "Laboratory values should always be interpreted by a qualified healthcare professional in combination "
            "with symptoms, medical history, medications, and clinical examination."
    },

    "glucose": {
        "min": 70,
        "max": 100,
        "critical_low": 50,
        "critical_high": 400,
        "unit": "mg/dL",
        "severity_low": "high",
        "severity_high": "high",
        "low_msg":
            "Your fasting blood glucose level is below the normal reference range. "
            "This condition is referred to as hypoglycemia. "
            "Low blood sugar can cause symptoms such as shakiness, sweating, dizziness, palpitations, "
            "confusion, and in severe cases, loss of consciousness. "
            "Common causes include prolonged fasting, skipping meals, excess insulin or diabetes medications, "
            "or certain medical conditions affecting glucose regulation.",
        "high_msg":
            "Your fasting blood glucose level is above the normal reference range. "
            "Elevated fasting glucose may indicate prediabetes or type 2 diabetes and should not be ignored. "
            "Chronically high blood sugar can cause long-term damage to the kidneys, eyes, nerves, "
            "and cardiovascular system. "
            "It is important to have this result evaluated further with your healthcare provider.",
        "normal_msg":
            "Your fasting blood glucose is within the normal reference range. "
            "This suggests that your body is managing blood sugar levels effectively at the time of testing, "
            "which is a positive indicator of metabolic health.",
        "what_it_means_low": [
            "Hypoglycemia can cause immediate symptoms such as trembling, sweating, and confusion",
            "Often triggered by missed meals, excess physical activity, or diabetes medications",
            "Severe hypoglycemia can be a medical emergency requiring immediate sugar intake",
            "Recurrent low glucose should be evaluated for underlying hormonal or metabolic causes"
        ],
        "what_it_means_high": [
            "Fasting glucose between 100 to 125 mg/dL suggests prediabetes",
            "Fasting glucose of 126 mg/dL or higher on two occasions is diagnostic of diabetes",
            "Chronically high glucose can damage blood vessels, kidneys, and nerves over time",
            "May also occur transiently due to illness, stress, or steroid medications"
        ],
        "eat": [
            "Whole grains such as brown rice, oats, and whole wheat bread",
            "High-fiber vegetables like broccoli, leafy greens, and cucumbers",
            "Nuts, seeds, and legumes for slow-releasing carbohydrates",
            "Low-glycemic index fruits such as apples, pears, and berries"
        ],
        "avoid": [
            "Sugary beverages such as soft drinks, fruit juices, and energy drinks",
            "Refined carbohydrates such as white bread, white rice, and pastries",
            "Deep-fried or heavily processed fast food",
            "Late-night heavy meals and irregular eating patterns"
        ],
        "tips": [
            "Engage in regular physical activity to improve insulin sensitivity",
            "Avoid long gaps between meals to maintain stable blood sugar levels",
            "Monitor your blood glucose regularly if you are at risk for diabetes",
            "Maintain a healthy body weight through balanced diet and exercise"
        ],
        "see_doctor_if": [
            "Your fasting glucose is consistently above 100 mg/dL",
            "You experience frequent dizziness, shakiness, or fainting episodes",
            "You notice increased thirst, frequent urination, or unexplained weight changes",
            "You have a family history of diabetes and have not had a recent evaluation"
        ],
        "related_tests": ["hba1c"],
        "did_you_know":
            "The brain is almost entirely dependent on glucose for energy and consumes approximately 20 percent of the body's total glucose supply at rest.",
        "category": "Diabetes",
        "emoji": "🍬",
        "medical_disclaimer":
            "This AI-generated interpretation is intended for informational and educational purposes only. "
            "Laboratory values should always be interpreted by a qualified healthcare professional in combination "
            "with symptoms, medical history, medications, and clinical examination."
    },

    "hba1c": {
        "min": 4.0,
        "max": 5.6,
        "critical_low": 3.0,
        "critical_high": 10.0,
        "unit": "%",
        "severity_low": "low",
        "severity_high": "high",
        "low_msg":
            "Your HbA1c level is lower than the standard reference range. "
            "While this is not typically a cause for major concern, very low HbA1c values may occasionally "
            "suggest recurrent hypoglycemia (low blood sugar episodes), excess diabetes medication, "
            "certain blood disorders, or laboratory variation. "
            "A discussion with your doctor is recommended to interpret this in context.",
        "high_msg":
            "Your HbA1c level is above the normal reference range. "
            "HbA1c reflects your average blood glucose control over the preceding two to three months. "
            "An elevated result may indicate prediabetes (5.7 to 6.4 percent) or diabetes (6.5 percent and above). "
            "Persistently high HbA1c is associated with an increased risk of complications affecting "
            "the kidneys, eyes, nerves, and cardiovascular system. "
            "This result warrants a formal evaluation by your healthcare provider.",
        "normal_msg":
            "Your HbA1c is within the healthy range, indicating that your average blood glucose levels "
            "over the past two to three months have been well-controlled. "
            "This is a reassuring sign of good long-term metabolic health.",
        "what_it_means_low": [
            "May suggest periods of recurrent low blood sugar over recent months",
            "Can occur with excessive diabetes medication or insulin in diabetic patients",
            "Certain blood conditions such as hemolytic anemia can falsely lower HbA1c",
            "Should be discussed with a doctor if unexpectedly low"
        ],
        "what_it_means_high": [
            "HbA1c of 5.7 to 6.4 percent indicates prediabetes, a reversible at-risk state",
            "HbA1c of 6.5 percent or above on two occasions is diagnostic of type 2 diabetes",
            "Sustained hyperglycemia can damage small blood vessels in the kidneys, retina, and nerves",
            "Reflects cumulative glucose exposure, making it a more reliable indicator than single glucose tests"
        ],
        "eat": [
            "High-fiber foods such as oats, legumes, and non-starchy vegetables",
            "Whole grain cereals and multi-grain bread",
            "Lean proteins such as fish, eggs, and pulses",
            "Healthy fats such as nuts, seeds, and olive oil"
        ],
        "avoid": [
            "Sugary beverages and sweetened juices",
            "Refined carbohydrates including white bread, pasta, and sweets",
            "Frequent desserts and sugar-laden processed snacks",
            "Sedentary habits and irregular meal timings"
        ],
        "tips": [
            "Monitor blood glucose regularly if you have diabetes or prediabetes",
            "Exercise for at least 30 minutes most days of the week",
            "Follow a consistent low-glycemic diet plan as guided by your doctor or dietitian",
            "Do not adjust diabetes medications without consulting your healthcare provider"
        ],
        "see_doctor_if": [
            "Your HbA1c is at or above 6.5 percent",
            "You experience increased thirst, frequent urination, or unexpected weight loss",
            "You have blurry vision, numbness in feet, or slow-healing wounds",
            "You have a family history of diabetes and have not been recently screened"
        ],
        "related_tests": ["glucose"],
        "did_you_know":
            "HbA1c measures the percentage of hemoglobin proteins in the blood that have glucose attached to them, providing a reliable three-month average of blood sugar control.",
        "category": "Diabetes",
        "emoji": "📉",
        "medical_disclaimer":
            "This AI-generated interpretation is intended for informational and educational purposes only. "
            "Laboratory values should always be interpreted by a qualified healthcare professional in combination "
            "with symptoms, medical history, medications, and clinical examination."
    },

    "cholesterol": {
        "min": 0,
        "max": 200,
        "critical_low": 0,
        "critical_high": 300,
        "unit": "mg/dL",
        "severity_low": "low",
        "severity_high": "high",
        "low_msg":
            "Your total cholesterol level is on the lower end. "
            "Very low cholesterol is generally not considered harmful in most individuals, "
            "but in rare cases, it has been associated with poor nutritional status or certain medical conditions. "
            "If your levels are extremely low, it may be worth discussing with your doctor.",
        "high_msg":
            "Your total cholesterol level is above the desirable range. "
            "High cholesterol, also known as hypercholesterolemia, is a significant risk factor for "
            "coronary artery disease, heart attack, and stroke. "
            "Elevated cholesterol often has no symptoms, which is why regular testing is important. "
            "It can result from an unhealthy diet, physical inactivity, obesity, genetics, or underlying conditions "
            "such as hypothyroidism and diabetes.",
        "normal_msg":
            "Your total cholesterol is within the desirable range. "
            "This is a positive indicator for cardiovascular health. "
            "Maintaining healthy cholesterol levels reduces the risk of heart disease and stroke.",
        "what_it_means_low": [
            "Very low cholesterol is rarely clinically significant",
            "May occasionally be associated with malnutrition, hyperthyroidism, or liver disease",
            "Generally not a concern unless associated with other abnormal findings"
        ],
        "what_it_means_high": [
            "High LDL cholesterol contributes to plaque buildup in arteries over time",
            "Can significantly increase the risk of heart attack and stroke",
            "Genetics can play a role, as seen in familial hypercholesterolemia",
            "Dietary habits, physical inactivity, and obesity are modifiable risk factors"
        ],
        "eat": [
            "Oats and oat bran, rich in soluble fiber that binds cholesterol",
            "Avocados and olive oil, which contain heart-healthy unsaturated fats",
            "Fatty fish such as salmon and mackerel, rich in omega-3 fatty acids",
            "Nuts especially almonds and walnuts",
            "Fruits and vegetables rich in antioxidants and fiber"
        ],
        "avoid": [
            "Deep-fried foods and foods high in saturated and trans fats",
            "Processed meats such as sausages, bacon, and salami",
            "Packaged snacks, cookies, and commercially baked goods",
            "Excess red meat consumption"
        ],
        "tips": [
            "Engage in at least 150 minutes of moderate aerobic activity per week",
            "Maintain a healthy body weight to help regulate cholesterol levels",
            "Quit smoking, as it lowers HDL (good cholesterol) and damages blood vessels",
            "Get a complete lipid panel including LDL, HDL, and triglycerides for a fuller picture"
        ],
        "see_doctor_if": [
            "Your total cholesterol is consistently above 200 mg/dL",
            "You have additional risk factors such as high blood pressure or diabetes",
            "You experience chest pain, tightness, or shortness of breath",
            "You have a family history of early heart disease"
        ],
        "related_tests": ["glucose", "hba1c"],
        "did_you_know":
            "Not all cholesterol is harmful. HDL cholesterol, often called good cholesterol, actually helps remove excess cholesterol from the bloodstream and transport it back to the liver.",
        "category": "Heart Health",
        "emoji": "❤️",
        "medical_disclaimer":
            "This AI-generated interpretation is intended for informational and educational purposes only. "
            "Laboratory values should always be interpreted by a qualified healthcare professional in combination "
            "with symptoms, medical history, medications, and clinical examination."
    },

    "creatinine": {
        "min": 0.6,
        "max": 1.2,
        "critical_low": 0.3,
        "critical_high": 5.0,
        "unit": "mg/dL",
        "severity_low": "low",
        "severity_high": "high",
        "low_msg":
            "Your creatinine level is slightly below the normal reference range. "
            "Low creatinine is typically not a major clinical concern and may be seen in individuals "
            "with low muscle mass, elderly patients, during pregnancy, or in those following a strict vegetarian diet. "
            "It is generally not considered dangerous but can be noted for clinical context.",
        "high_msg":
            "Your creatinine level is above the normal reference range. "
            "Creatinine is a waste product produced by normal muscle metabolism and is filtered from the blood "
            "by the kidneys. Elevated creatinine may indicate impaired kidney function or reduced filtration capacity. "
            "Possible causes include dehydration, kidney disease, high protein intake, certain medications, "
            "or conditions such as diabetes and hypertension that affect the kidneys over time. "
            "This result should be evaluated further by your healthcare provider.",
        "normal_msg":
            "Your creatinine level is within the normal range. "
            "This suggests that your kidneys are likely filtering waste from the blood at a normal rate, "
            "which is a positive indicator of kidney health.",
        "what_it_means_low": [
            "Often seen in elderly individuals or those with reduced muscle mass",
            "Can occur during pregnancy due to increased kidney filtration",
            "Generally not clinically significant in isolation"
        ],
        "what_it_means_high": [
            "May indicate acute or chronic kidney disease",
            "Dehydration can temporarily raise creatinine by reducing kidney perfusion",
            "Long-standing diabetes and hypertension are leading causes of kidney damage",
            "High creatinine is often accompanied by symptoms such as swelling, fatigue, or reduced urine output"
        ],
        "eat": [
            "Fresh fruits and vegetables which are low in protein and easy on the kidneys",
            "Low-sodium foods to reduce blood pressure strain on the kidneys",
            "Adequate water intake to maintain kidney filtration",
            "Foods with controlled potassium and phosphorus if advised by a doctor"
        ],
        "avoid": [
            "Excess salt and sodium-rich processed foods",
            "Very high protein diets or excess red meat consumption",
            "Excess protein supplements or creatine supplements without medical guidance",
            "Medications such as NSAIDs that can impair kidney function if taken excessively"
        ],
        "tips": [
            "Stay well hydrated throughout the day",
            "Monitor blood pressure and blood sugar regularly, as both affect kidney health",
            "Avoid self-medicating with painkillers that can damage the kidneys",
            "Follow up with kidney function tests as recommended by your doctor"
        ],
        "see_doctor_if": [
            "You notice swelling in your feet, ankles, or around your eyes",
            "You have reduced urine output or foamy urine",
            "Your creatinine is persistently elevated on repeated testing",
            "You have a history of diabetes, hypertension, or known kidney disease"
        ],
        "related_tests": ["sodium", "potassium", "bilirubin"],
        "did_you_know":
            "Creatinine is produced at a fairly constant rate by muscle cells, making it a reliable marker for estimating how well your kidneys are filtering your blood.",
        "category": "Kidney Function",
        "emoji": "💧",
        "medical_disclaimer":
            "This AI-generated interpretation is intended for informational and educational purposes only. "
            "Laboratory values should always be interpreted by a qualified healthcare professional in combination "
            "with symptoms, medical history, medications, and clinical examination."
    },

    "tsh": {
        "min": 0.4,
        "max": 4.0,
        "critical_low": 0.1,
        "critical_high": 10.0,
        "unit": "mIU/L",
        "severity_low": "moderate",
        "severity_high": "moderate",
        "low_msg":
            "Your TSH (Thyroid Stimulating Hormone) level is below the normal reference range. "
            "Low TSH may indicate an overactive thyroid gland, a condition known as hyperthyroidism, "
            "where the thyroid produces excess hormones. "
            "This can cause symptoms such as unexplained weight loss, rapid or irregular heartbeat, "
            "anxiety, sweating, tremors, and difficulty sleeping. "
            "A low TSH can also occur with excess thyroid hormone replacement medication.",
        "high_msg":
            "Your TSH level is above the normal reference range. "
            "Elevated TSH typically indicates an underactive thyroid gland, a condition known as hypothyroidism, "
            "where the thyroid does not produce sufficient hormones. "
            "Symptoms may include unexplained weight gain, persistent fatigue, cold intolerance, dry skin, "
            "hair thinning, constipation, and low mood. "
            "Hypothyroidism is a manageable condition and usually responds well to appropriate treatment.",
        "normal_msg":
            "Your TSH level is within the normal reference range. "
            "This suggests that your thyroid gland is likely functioning normally and "
            "producing thyroid hormones at an appropriate level for your body's needs.",
        "what_it_means_low": [
            "Low TSH often points to hyperthyroidism or excess thyroid hormone intake",
            "Can cause anxiety, rapid heartbeat, weight loss, and heat intolerance",
            "May also be seen in early pregnancy or with certain pituitary gland conditions",
            "Requires further testing with free T3 and free T4 to confirm the cause"
        ],
        "what_it_means_high": [
            "High TSH indicates the pituitary is signaling the thyroid to produce more hormone",
            "Suggestive of primary hypothyroidism, most commonly due to autoimmune thyroiditis",
            "Can cause weight gain, fatigue, cold sensitivity, and cognitive slowing",
            "Requires free T4 testing and possibly thyroid antibody testing for full evaluation"
        ],
        "eat": [
            "Iodine-rich foods such as seafood, dairy, and iodized salt in moderate amounts",
            "Selenium-rich foods such as Brazil nuts, sunflower seeds, and fish",
            "Adequate protein from eggs, legumes, and lean meats",
            "Zinc-containing foods such as pumpkin seeds and whole grains"
        ],
        "avoid": [
            "Excess raw cruciferous vegetables such as cabbage and cauliflower for those with hypothyroidism",
            "Soy products in large amounts if on thyroid medication",
            "Unnecessary thyroid supplements without confirmed deficiency",
            "Highly processed junk foods that provide little nutritional value"
        ],
        "tips": [
            "Take thyroid medication at the same time each day on an empty stomach if prescribed",
            "Get adequate sleep and manage stress, as both affect thyroid function",
            "Retest TSH every 6 to 12 months or as directed by your doctor",
            "Do not adjust thyroid medication doses without medical consultation"
        ],
        "see_doctor_if": [
            "You experience rapid heartbeat, anxiety, or sudden unexplained weight loss",
            "You notice persistent fatigue, weight gain, or cold intolerance",
            "Your TSH remains abnormal on repeated testing",
            "You are pregnant or planning pregnancy, as thyroid health is critical during this time"
        ],
        "related_tests": ["glucose", "cholesterol"],
        "did_you_know":
            "TSH is produced by the pituitary gland in the brain and acts as a messenger to tell the thyroid gland how much hormone to produce. It rises when thyroid hormone levels are low and falls when they are high.",
        "category": "Hormones",
        "emoji": "🦋",
        "medical_disclaimer":
            "This AI-generated interpretation is intended for informational and educational purposes only. "
            "Laboratory values should always be interpreted by a qualified healthcare professional in combination "
            "with symptoms, medical history, medications, and clinical examination."
    },

    "uric_acid": {
        "min": 3.5,
        "max": 7.2,
        "critical_low": 1.0,
        "critical_high": 12.0,
        "unit": "mg/dL",
        "severity_low": "low",
        "severity_high": "moderate",
        "low_msg":
            "Your uric acid level is slightly below the normal reference range. "
            "Low uric acid is generally not a significant clinical concern in most individuals. "
            "It can occasionally occur with certain medications, liver conditions, or dietary factors. "
            "If your levels are very low, your doctor may consider further evaluation based on your overall clinical picture.",
        "high_msg":
            "Your uric acid level is above the normal reference range. "
            "Elevated uric acid, known as hyperuricemia, occurs when the body either produces too much uric acid "
            "or the kidneys fail to excrete it efficiently. "
            "Chronically high levels can lead to the formation of urate crystals in the joints, "
            "causing painful inflammation known as gout. "
            "It can also contribute to the development of kidney stones and, in some studies, "
            "has been associated with cardiovascular risk.",
        "normal_msg":
            "Your uric acid level is within the normal range. "
            "This indicates that uric acid production and excretion appear to be appropriately balanced, "
            "reducing your risk of gout and uric acid-related kidney stones.",
        "what_it_means_low": [
            "Low uric acid is usually not clinically significant",
            "May occur with certain medications such as allopurinol or losartan",
            "Rarely associated with conditions affecting uric acid reabsorption in the kidneys"
        ],
        "what_it_means_high": [
            "Urate crystals can deposit in joints, particularly the big toe, ankle, and knee, causing gout attacks",
            "Can lead to recurrent kidney stones made of uric acid",
            "Commonly triggered by high intake of purine-rich foods, alcohol, or dehydration",
            "Associated with metabolic syndrome, hypertension, and obesity in some individuals"
        ],
        "eat": [
            "Plenty of water, at least 8 to 10 glasses per day, to help flush uric acid through kidneys",
            "Fresh fruits such as cherries, which may help reduce uric acid levels",
            "Low-fat dairy products, which have been associated with lower uric acid",
            "High-fiber vegetables and whole grains"
        ],
        "avoid": [
            "Red meat, organ meats such as liver and kidneys, and shellfish, which are high in purines",
            "Alcohol, especially beer and spirits, which raise uric acid levels significantly",
            "Sugary beverages and foods sweetened with high-fructose corn syrup",
            "Crash diets or prolonged fasting, which can transiently raise uric acid"
        ],
        "tips": [
            "Stay well hydrated to support renal uric acid excretion",
            "Maintain a healthy body weight through regular physical activity and a balanced diet",
            "Take medications such as allopurinol exactly as prescribed if recommended by your doctor",
            "Track and record any joint pain episodes to report to your healthcare provider"
        ],
        "see_doctor_if": [
            "You experience sudden severe joint pain, redness, or swelling particularly in the big toe",
            "You have had recurrent kidney stones",
            "Your uric acid level remains persistently elevated on repeated testing",
            "You have associated conditions such as hypertension, diabetes, or chronic kidney disease"
        ],
        "related_tests": ["creatinine"],
        "did_you_know":
            "Gout has historically been called the disease of kings because of its association with rich diets and alcohol, affecting notable historical figures including King Henry VIII.",
        "category": "Metabolism",
        "emoji": "🦴",
        "medical_disclaimer":
            "This AI-generated interpretation is intended for informational and educational purposes only. "
            "Laboratory values should always be interpreted by a qualified healthcare professional in combination "
            "with symptoms, medical history, medications, and clinical examination."
    },

    "sodium": {
        "min": 135,
        "max": 145,
        "critical_low": 120,
        "critical_high": 160,
        "unit": "mEq/L",
        "severity_low": "high",
        "severity_high": "high",
        "low_msg":
            "Your blood sodium level is below the normal reference range, a condition known as hyponatremia. "
            "Sodium is a critical electrolyte that regulates fluid balance, nerve impulse transmission, "
            "and muscle contraction. "
            "Low sodium can cause symptoms ranging from mild nausea and headache to severe confusion, "
            "seizures, or loss of consciousness in extreme cases. "
            "Common causes include excessive water intake, vomiting and diarrhea, certain medications "
            "such as diuretics, kidney disease, or hormonal imbalances.",
        "high_msg":
            "Your blood sodium level is above the normal reference range, a condition known as hypernatremia. "
            "Elevated sodium usually indicates inadequate fluid intake or excess fluid loss, "
            "leading to a relative concentration of sodium in the blood. "
            "Symptoms may include intense thirst, dry mouth, restlessness, and in severe cases, "
            "neurological symptoms such as confusion or seizures. "
            "This condition requires prompt identification and correction of the underlying cause.",
        "normal_msg":
            "Your sodium level is within the normal range. "
            "This suggests that your body's fluid and electrolyte balance is likely being well maintained, "
            "supporting normal nerve and muscle function.",
        "what_it_means_low": [
            "Hyponatremia can cause cellular swelling as water moves into cells due to osmotic shifts",
            "Neurological symptoms such as confusion, headache, and seizures can occur with severe drops",
            "Diuretics, heart failure, liver cirrhosis, and kidney disease are common causes",
            "Drinking excess plain water during prolonged exercise can also trigger hyponatremia"
        ],
        "what_it_means_high": [
            "Usually reflects dehydration or inadequate fluid replacement",
            "Can also occur with diabetes insipidus, diarrhea, or excess sodium intake",
            "High sodium causes cells to shrink as water moves out, potentially affecting brain cells",
            "Requires gradual fluid correction to avoid dangerous complications"
        ],
        "eat": [
            "Water-rich fruits and vegetables to maintain hydration",
            "Balanced electrolyte-containing foods",
            "Oral rehydration solutions if experiencing fluid losses due to illness",
            "Moderate natural sources of sodium through food rather than added salt"
        ],
        "avoid": [
            "Excess salty snacks, pickles, and processed packaged foods",
            "Overuse of table salt or sodium-heavy condiments",
            "Excessive plain water intake during prolonged physical activity without electrolyte replacement"
        ],
        "tips": [
            "Maintain consistent and adequate daily hydration",
            "Monitor sodium levels if you are on diuretics or have kidney or heart disease",
            "Use oral rehydration solutions rather than plain water during severe vomiting or diarrhea",
            "Report symptoms of extreme weakness, confusion, or muscle cramps to your doctor promptly"
        ],
        "see_doctor_if": [
            "You feel confused, disoriented, or have a severe headache",
            "You experience muscle cramps, weakness, or seizures",
            "Your sodium is critically outside the normal range",
            "You are on diuretics or have conditions affecting fluid balance"
        ],
        "related_tests": ["potassium", "creatinine"],
        "did_you_know":
            "Sodium is so essential to life that the body has multiple hormonal systems dedicated entirely to regulating its concentration, including the renin-angiotensin-aldosterone system.",
        "category": "Electrolytes",
        "emoji": "⚡",
        "medical_disclaimer":
            "This AI-generated interpretation is intended for informational and educational purposes only. "
            "Laboratory values should always be interpreted by a qualified healthcare professional in combination "
            "with symptoms, medical history, medications, and clinical examination."
    },

    "potassium": {
        "min": 3.5,
        "max": 5.0,
        "critical_low": 2.5,
        "critical_high": 6.5,
        "unit": "mEq/L",
        "severity_low": "high",
        "severity_high": "high",
        "low_msg":
            "Your blood potassium level is below the normal reference range, a condition called hypokalemia. "
            "Potassium is essential for maintaining normal heart rhythm, muscle contraction, "
            "and nerve signal transmission. "
            "Low potassium can cause muscle weakness, cramps, fatigue, constipation, and heart rhythm disturbances. "
            "Common causes include prolonged vomiting or diarrhea, excessive sweating, diuretic use, "
            "poor dietary intake, or certain kidney conditions.",
        "high_msg":
            "Your blood potassium level is above the normal reference range, a condition called hyperkalemia. "
            "Elevated potassium is a potentially serious finding, particularly because it can disrupt the heart's "
            "electrical conduction system and lead to dangerous arrhythmias. "
            "Causes may include kidney insufficiency, use of certain medications, excessive supplementation, "
            "or conditions that cause cells to release potassium into the bloodstream such as significant tissue injury.",
        "normal_msg":
            "Your potassium level is within the normal range. "
            "This is reassuring for normal heart rhythm, nerve function, and muscle performance.",
        "what_it_means_low": [
            "Hypokalemia can cause muscle weakness, cramps, and fatigue",
            "Significant drops in potassium can trigger dangerous cardiac arrhythmias",
            "Common triggers include diarrhea, vomiting, heavy sweating, and diuretic medications",
            "Insulin and certain hormones can also shift potassium from blood into cells, lowering blood levels"
        ],
        "what_it_means_high": [
            "Hyperkalemia is potentially life-threatening as it can cause fatal heart rhythm disturbances",
            "Most commonly seen in patients with reduced kidney function",
            "Certain medications such as ACE inhibitors, potassium-sparing diuretics, and NSAIDs can raise potassium",
            "Cell destruction from trauma or severe illness can also release potassium into the bloodstream"
        ],
        "eat": [
            "Bananas, oranges, and kiwis as natural potassium sources when levels are low",
            "Coconut water as a natural electrolyte replenisher",
            "Leafy greens such as spinach and sweet potato",
            "Legumes and beans for steady potassium intake"
        ],
        "avoid": [
            "Excess potassium supplements without medical supervision",
            "Salt substitutes containing potassium chloride, especially if on certain medications",
            "Excess processed foods which can disrupt electrolyte balance",
            "Overexertion without adequate electrolyte replacement"
        ],
        "tips": [
            "Maintain consistent hydration and a balanced diet",
            "If on diuretics, ask your doctor whether potassium monitoring or supplementation is needed",
            "Report muscle cramps, palpitations, or irregular heartbeat to your doctor immediately",
            "Avoid making dietary changes significantly high in potassium without medical guidance if you have kidney disease"
        ],
        "see_doctor_if": [
            "You experience chest pain, palpitations, or irregular heartbeat",
            "You have severe muscle weakness or paralysis",
            "Your potassium is in the critical low or high range",
            "You are on medications that commonly affect potassium levels"
        ],
        "related_tests": ["sodium", "creatinine"],
        "did_you_know":
            "The heart muscle is extremely sensitive to potassium levels. Even small changes outside the normal range can significantly affect the heart's electrical activity and rhythm.",
        "category": "Electrolytes",
        "emoji": "🍌",
        "medical_disclaimer":
            "This AI-generated interpretation is intended for informational and educational purposes only. "
            "Laboratory values should always be interpreted by a qualified healthcare professional in combination "
            "with symptoms, medical history, medications, and clinical examination."
    },

    "bilirubin": {
        "min": 0.1,
        "max": 1.2,
        "critical_low": 0.0,
        "critical_high": 5.0,
        "unit": "mg/dL",
        "severity_low": "low",
        "severity_high": "high",
        "low_msg":
            "Your bilirubin level is very low, which is not typically considered a medical concern. "
            "Very low bilirubin levels are generally not clinically significant and do not usually "
            "require any specific intervention.",
        "high_msg":
            "Your bilirubin level is above the normal reference range. "
            "Bilirubin is a yellow-orange pigment produced when red blood cells are broken down. "
            "It is processed by the liver and excreted through bile. "
            "Elevated bilirubin may indicate liver disease such as hepatitis or cirrhosis, "
            "obstruction of bile ducts, or excessive breakdown of red blood cells. "
            "Clinically, high bilirubin can cause jaundice, which is a yellowish discoloration of the skin and eyes.",
        "normal_msg":
            "Your bilirubin level is within the normal range. "
            "This suggests that your liver is processing and excreting bilirubin effectively, "
            "indicating healthy liver and bile duct function.",
        "what_it_means_low": [
            "Very low bilirubin is generally not medically significant",
            "No clinical action is usually required for isolated low bilirubin"
        ],
        "what_it_means_high": [
            "Elevated bilirubin can cause jaundice, visible as yellow discoloration of skin and eyes",
            "May indicate liver inflammation, hepatitis, cirrhosis, or bile duct obstruction",
            "Hemolytic anemia, where red blood cells are destroyed faster than normal, also raises bilirubin",
            "Gilbert syndrome is a benign inherited condition that causes mildly elevated bilirubin without liver disease"
        ],
        "eat": [
            "Fresh fruits and vegetables that support liver detoxification",
            "Light, home-cooked, easily digestible meals",
            "Adequate water intake to support bilirubin excretion",
            "Turmeric in moderate amounts, which may have liver-protective properties"
        ],
        "avoid": [
            "Alcohol, which places additional stress on the liver",
            "Excess oily, fried, or heavy foods",
            "Unnecessary medications or supplements without medical guidance",
            "Prolonged fasting, which can transiently raise bilirubin in susceptible individuals"
        ],
        "tips": [
            "Maintain good liver health through a balanced diet and limited alcohol consumption",
            "Stay well hydrated to support liver and kidney function",
            "Report any yellowing of skin or eyes to your doctor immediately",
            "Get a complete liver function test panel for a comprehensive assessment"
        ],
        "see_doctor_if": [
            "Your skin or eyes appear yellow",
            "You experience persistent nausea, abdominal pain, or dark-colored urine",
            "You have pale or clay-colored stools",
            "Bilirubin remains elevated on repeated testing"
        ],
        "related_tests": ["sgpt", "sgot"],
        "did_you_know":
            "Bilirubin is actually what gives bruises their characteristic yellow-green color as they heal, and it is also responsible for the yellow color of urine.",
        "category": "Liver Function",
        "emoji": "🟡",
        "medical_disclaimer":
            "This AI-generated interpretation is intended for informational and educational purposes only. "
            "Laboratory values should always be interpreted by a qualified healthcare professional in combination "
            "with symptoms, medical history, medications, and clinical examination."
    },

    "sgpt": {
        "min": 7,
        "max": 56,
        "critical_low": 0,
        "critical_high": 200,
        "unit": "U/L",
        "severity_low": "low",
        "severity_high": "high",
        "low_msg":
            "Your SGPT (Serum Glutamate Pyruvate Transaminase), also known as ALT (Alanine Aminotransferase), "
            "is within or below the normal range. "
            "Low SGPT is typically not a clinical concern and requires no specific action.",
        "high_msg":
            "Your SGPT level is above the normal reference range. "
            "SGPT is an enzyme found predominantly in liver cells. "
            "When liver cells are damaged or inflamed, SGPT is released into the bloodstream, "
            "causing elevated blood levels. "
            "Common causes include non-alcoholic fatty liver disease (NAFLD), viral hepatitis, "
            "alcohol-related liver injury, use of certain medications, or metabolic syndrome. "
            "The degree of elevation can help guide further investigation.",
        "normal_msg":
            "Your SGPT level is within the normal range. "
            "This is a reassuring indicator of liver health, suggesting no significant liver cell damage "
            "at the time of testing.",
        "what_it_means_low": [
            "Low SGPT is generally not clinically significant",
            "No action required in most cases when the value is simply at the lower end"
        ],
        "what_it_means_high": [
            "SGPT is the most specific liver enzyme marker for hepatocellular damage",
            "Non-alcoholic fatty liver disease is the most common cause of mildly elevated SGPT",
            "Viral hepatitis A, B, and C can cause moderate to markedly elevated levels",
            "Certain medications including statins, antibiotics, and herbal supplements can raise SGPT"
        ],
        "eat": [
            "Fresh fruits and vegetables rich in antioxidants",
            "Green tea in moderate amounts, which may support liver health",
            "Light, easily digestible home-cooked meals",
            "Foods rich in Vitamin E such as nuts and seeds"
        ],
        "avoid": [
            "Alcohol and alcohol-containing beverages in any amount",
            "Excess oily, fried, and fatty foods",
            "Unnecessary over-the-counter medications and herbal supplements without medical advice",
            "Highly processed and sugary foods that contribute to fatty liver"
        ],
        "tips": [
            "Maintain a healthy body weight to reduce risk of fatty liver disease",
            "Exercise regularly to improve liver metabolism",
            "Avoid alcohol completely until levels normalize",
            "Repeat liver function tests as advised by your doctor to monitor trends"
        ],
        "see_doctor_if": [
            "Your SGPT is significantly elevated or rising on repeat tests",
            "You experience abdominal pain, nausea, or jaundice",
            "You are taking medications that are known to affect liver enzymes",
            "You have risk factors for viral hepatitis or fatty liver disease"
        ],
        "related_tests": ["sgot", "bilirubin"],
        "did_you_know":
            "SGPT is considered the most sensitive and specific blood test for detecting liver cell injury, which is why it is often the first abnormality seen in liver disease.",
        "category": "Liver Function",
        "emoji": "🧪",
        "medical_disclaimer":
            "This AI-generated interpretation is intended for informational and educational purposes only. "
            "Laboratory values should always be interpreted by a qualified healthcare professional in combination "
            "with symptoms, medical history, medications, and clinical examination."
    },

    "sgot": {
        "min": 8,
        "max": 48,
        "critical_low": 0,
        "critical_high": 200,
        "unit": "U/L",
        "severity_low": "low",
        "severity_high": "high",
        "low_msg":
            "Your SGOT (Serum Glutamate Oxaloacetate Transaminase), also known as AST (Aspartate Aminotransferase), "
            "is within or below the normal range. "
            "Low SGOT is generally not a clinical concern.",
        "high_msg":
            "Your SGOT level is above the normal reference range. "
            "SGOT is an enzyme present not only in the liver but also in heart muscle, skeletal muscle, "
            "kidneys, and red blood cells. "
            "Elevated SGOT may therefore indicate liver damage, muscle injury, heart conditions, "
            "or intense physical exertion. "
            "When SGOT is raised alongside SGPT, a liver cause is more likely. "
            "When SGOT is disproportionately raised, heart or muscle causes should be considered. "
            "Further testing will help clarify the source.",
        "normal_msg":
            "Your SGOT level is within the normal range. "
            "This suggests no significant liver or muscle damage is evident from this marker at the time of testing.",
        "what_it_means_low": [
            "Low SGOT is generally not clinically significant",
            "No specific action is needed in isolation"
        ],
        "what_it_means_high": [
            "When elevated with SGPT, suggests liver cell damage from hepatitis, fatty liver, or alcohol",
            "When elevated alone, may suggest cardiac injury, muscle damage, or strenuous exercise",
            "Chronic alcohol use typically causes a disproportionate rise in SGOT relative to SGPT",
            "Certain medications and supplements can also elevate SGOT"
        ],
        "eat": [
            "Balanced and nutritious home-cooked meals with plenty of fresh vegetables",
            "Antioxidant-rich foods such as berries, tomatoes, and leafy greens",
            "Whole grains and fiber-rich foods",
            "Adequate protein from lean, low-fat sources"
        ],
        "avoid": [
            "Alcohol in all forms",
            "Unnecessary supplements and herbal remedies without medical supervision",
            "Excess fatty or fried foods",
            "Overexertion immediately before a blood test, as strenuous exercise can raise SGOT transiently"
        ],
        "tips": [
            "Monitor liver health through regular liver function tests",
            "Reduce alcohol intake or abstain completely if levels are elevated",
            "Report all medications and supplements to your doctor for review",
            "Maintain a healthy lifestyle with regular exercise and a balanced diet"
        ],
        "see_doctor_if": [
            "SGOT remains persistently elevated or is significantly raised",
            "You experience abdominal discomfort, yellowing of eyes, or unexplained fatigue",
            "You have recently had chest pain or a possible cardiac event",
            "Your SGOT is rising alongside other abnormal liver or cardiac markers"
        ],
        "related_tests": ["sgpt", "bilirubin"],
        "did_you_know":
            "SGOT is found in many tissues throughout the body, which is why doctors often look at the SGOT to SGPT ratio to help distinguish between liver disease and other causes of enzyme elevation.",
        "category": "Liver Function",
        "emoji": "🧬",
        "medical_disclaimer":
            "This AI-generated interpretation is intended for informational and educational purposes only. "
            "Laboratory values should always be interpreted by a qualified healthcare professional in combination "
            "with symptoms, medical history, medications, and clinical examination."
    },

    "vitamin_d": {
        "min": 20,
        "max": 50,
        "critical_low": 10,
        "critical_high": 100,
        "unit": "ng/mL",
        "severity_low": "moderate",
        "severity_high": "moderate",
        "low_msg":
            "Your Vitamin D level is below the recommended reference range. "
            "Vitamin D is a fat-soluble vitamin that plays a critical role in calcium absorption, "
            "bone mineralization, immune function, and muscle strength. "
            "Deficiency is extremely common, particularly in individuals with limited sun exposure, "
            "darker skin tones, or those who spend most of their time indoors. "
            "Symptoms of Vitamin D deficiency may include bone pain, muscle weakness, fatigue, "
            "low mood, and increased susceptibility to infections.",
        "high_msg":
            "Your Vitamin D level is above the normal upper limit. "
            "Vitamin D toxicity, known as hypervitaminosis D, is almost always caused by excessive supplementation "
            "rather than sun exposure, as the body regulates sun-derived Vitamin D production naturally. "
            "Very high Vitamin D levels can raise calcium levels in the blood, "
            "potentially causing nausea, vomiting, weakness, frequent urination, kidney stones, "
            "or in severe cases, damage to the kidneys and heart.",
        "normal_msg":
            "Your Vitamin D level is within the recommended range. "
            "This is a positive finding indicating adequate Vitamin D status for supporting bone health, "
            "immune function, and overall wellbeing.",
        "what_it_means_low": [
            "Low Vitamin D impairs calcium absorption, weakening bones and increasing fracture risk",
            "Associated with increased risk of osteoporosis and osteomalacia in adults",
            "Linked to muscle weakness, fatigue, and low mood in some individuals",
            "Inadequate sun exposure is the most common cause globally"
        ],
        "what_it_means_high": [
            "Vitamin D toxicity is rare and almost exclusively caused by excessive supplementation",
            "Can raise blood calcium levels, leading to hypercalcemia",
            "Symptoms of toxicity include nausea, weakness, confusion, and excessive urination",
            "Long-standing toxicity can damage kidneys and blood vessels"
        ],
        "eat": [
            "Fatty fish such as salmon, sardines, and mackerel",
            "Egg yolks and liver in moderate amounts",
            "Vitamin D fortified dairy products, plant milks, and cereals",
            "Mushrooms exposed to sunlight, which naturally contain Vitamin D"
        ],
        "avoid": [
            "Excess Vitamin D supplements beyond the prescribed dose",
            "Taking supplements without confirming deficiency through blood tests",
            "Remaining completely indoors without any sunlight exposure"
        ],
        "tips": [
            "Aim for 15 to 30 minutes of morning sunlight exposure on uncovered skin several days per week",
            "Take Vitamin D supplements as prescribed by your doctor, preferably with a fatty meal for better absorption",
            "Pair Vitamin D intake with adequate calcium and Vitamin K2 for optimal bone health",
            "Recheck Vitamin D levels after 3 months of supplementation to assess response"
        ],
        "see_doctor_if": [
            "You experience persistent bone pain, joint aches, or frequent stress fractures",
            "You feel chronically fatigued despite adequate rest",
            "Your levels remain critically low despite supplementation",
            "You are taking high-dose supplements and experience nausea, weakness, or confusion"
        ],
        "related_tests": ["calcium"],
        "did_you_know":
            "Vitamin D is unique among vitamins because the human body can synthesize it naturally when the skin is exposed to sunlight, technically making it more of a hormone than a traditional vitamin.",
        "category": "Vitamins",
        "emoji": "☀️",
        "medical_disclaimer":
            "This AI-generated interpretation is intended for informational and educational purposes only. "
            "Laboratory values should always be interpreted by a qualified healthcare professional in combination "
            "with symptoms, medical history, medications, and clinical examination."
    },

    "calcium": {
        "min": 8.5,
        "max": 10.5,
        "critical_low": 6.0,
        "critical_high": 13.0,
        "unit": "mg/dL",
        "severity_low": "high",
        "severity_high": "high",
        "low_msg":
            "Your blood calcium level is below the normal reference range, a condition called hypocalcemia. "
            "Calcium is essential for bone structure, muscle contraction, nerve transmission, "
            "and many cellular processes. "
            "Low calcium may cause muscle cramps and spasms, tingling or numbness around the mouth and in the fingers, "
            "irritability, and in severe cases, abnormal heart rhythms or seizures. "
            "Common causes include Vitamin D deficiency, hypoparathyroidism, kidney disease, or poor dietary intake.",
        "high_msg":
            "Your blood calcium level is above the normal reference range, a condition called hypercalcemia. "
            "Excess calcium in the blood can occur due to overactive parathyroid glands (hyperparathyroidism), "
            "excess Vitamin D supplementation, certain cancers, prolonged immobilization, "
            "or excessive calcium supplement intake. "
            "Symptoms can include fatigue, nausea, constipation, frequent urination, confusion, "
            "and in chronic cases, kidney stone formation.",
        "normal_msg":
            "Your blood calcium level is within the normal range. "
            "This is a reassuring finding indicating that calcium levels in your blood are well-regulated, "
            "supporting normal bone health, muscle function, and nerve activity.",
        "what_it_means_low": [
            "Hypocalcemia can cause tetany, characterized by involuntary muscle spasms and cramps",
            "Numbness and tingling, particularly around the lips and in the hands, are classic early symptoms",
            "Vitamin D deficiency is a very common underlying contributor to low calcium",
            "Hypoparathyroidism, a condition of insufficient parathyroid hormone, is another important cause"
        ],
        "what_it_means_high": [
            "Hyperparathyroidism is the most common cause of high calcium in outpatient settings",
            "Malignancies can release substances that raise blood calcium levels",
            "Excess Vitamin D or calcium supplement intake can cause hypercalcemia",
            "Symptoms often described as bones, stones, groans, and moans reflecting bone pain, kidney stones, abdominal discomfort, and depression"
        ],
        "eat": [
            "Dairy products such as milk, yogurt, and cheese for dietary calcium",
            "Sesame seeds, almonds, and tofu as plant-based calcium sources",
            "Dark leafy greens such as kale, bok choy, and broccoli",
            "Calcium-fortified plant milks and cereals"
        ],
        "avoid": [
            "Excess carbonated soft drinks which can interfere with calcium absorption",
            "Very high sodium diets which increase urinary calcium loss",
            "Excessive calcium supplements beyond recommended doses without medical guidance",
            "Excess Vitamin A supplementation, which can reduce bone density"
        ],
        "tips": [
            "Ensure adequate Vitamin D intake alongside calcium, as Vitamin D is essential for calcium absorption",
            "Engage in weight-bearing exercise such as walking and strength training to support bone health",
            "Avoid both deficiency and excess of calcium by following medically recommended daily intakes",
            "Monitor calcium levels periodically if you are on calcium or Vitamin D supplements"
        ],
        "see_doctor_if": [
            "You experience muscle cramps, spasms, or tingling in the extremities",
            "You have persistent fatigue, confusion, or mood changes",
            "You develop kidney stones or frequent urination",
            "Your calcium level is critically outside the normal range on testing"
        ],
        "related_tests": ["vitamin_d", "creatinine"],
        "did_you_know":
            "Approximately 99 percent of the body's calcium is stored in the bones and teeth, with only one percent circulating in the blood, yet this small fraction plays an enormous role in heart function, nerve signaling, and muscle activity.",
        "category": "Minerals",
        "emoji": "🦴",
        "medical_disclaimer":
            "This AI-generated interpretation is intended for informational and educational purposes only. "
            "Laboratory values should always be interpreted by a qualified healthcare professional in combination "
            "with symptoms, medical history, medications, and clinical examination."
    }

}