# 🩺 AI Medical Report Interpreter

An AI-powered healthcare assistant that helps users understand complex blood test reports in simple, human-readable language instead of raw medical numbers.

> ⚠️ **Actively under development** — new features are being added regularly.

---

## 🚀 Core Features

- 📄 **OCR Upload** – Extract data from medical reports (PDF/Image)
- 🧠 **AI Interpretation** – Smart analysis of blood test parameters
- ⚠️ **Severity Detection** – Normal / Low / High / Critical classification
- 🩺 **Doctor-style Explanations** – Causes, symptoms & next steps
- 🍎 **Food Recommendations** – Personalized diet suggestions
- 🌍 **Multilingual Support** – English, Hindi, Marathi (expanding)
- 💬 **Chat with Reports** – Ask questions like “Why is hemoglobin low?”
- 📈 **Health Trends** – Track improvements over time
- 🎨 **Dashboard UI** – Clean charts & visual insights
- 🏆 **Health Score** – Overall score (0–100) with breakdown  

---

## 🧪 Supported Blood Tests

| Category | Parameters |
|----------|------------|
| CBC | Hemoglobin, RBC, WBC, Platelets |
| Diabetes | Glucose, HbA1c |
| Lipid | Cholesterol, LDL, HDL, Triglycerides |
| Kidney | Creatinine, Uric Acid, Sodium, Potassium |
| Liver | Bilirubin, SGPT (ALT), SGOT (AST) |
| Thyroid | TSH |
| Vitamins | Vitamin D, Calcium |

Each parameter includes:
- Normal & critical ranges  
- Severity classification  
- Simple explanations  
- Diet suggestions 🍎  
- Symptoms to watch ⚠️  
- Doctor consultation triggers 🩺  

---

## 🧠 AI Interpretation Engine

This project uses a **hybrid intelligence system**:

- 📊 Rule-based medical range system (deterministic logic)
- 🤖 LLM layer (Gemini / OpenAI) for explanations
- 🧩 Combined reasoning for accurate + human-friendly output

---

## 📊 Sample Output

**Test:** Hemoglobin  
**Value:** 10.2 g/dL  
**Status:** Low ⚠️  

**Explanation:**  
You may have mild anemia, which can cause fatigue and weakness.

**Suggestions:**  
- Eat iron-rich foods 🥬  
- Increase Vitamin C intake 🍊  
- Consult a doctor if symptoms persist 🩺  

---


