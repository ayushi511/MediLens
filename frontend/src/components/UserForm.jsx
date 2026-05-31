import { useState } from "react";
function UserForm({ onSubmit }) {
    const [age, setAge] = useState("");
    const [gender, setGender] = useState("");
    const [pregnant, setPregnant] = useState(false);

    const handleSubmit = () => {
        if (!age || !gender) {
            alert("Please enter age and gender to get accurate results.");
            return;
        }
        onSubmit({ age: parseInt(age), gender, pregnant });
    };

    const ageNum = parseInt(age);
    const isChild = ageNum < 18;
    const isSenior = ageNum >= 60;

    return (
        <div style={{
            background: "#fff", border: "0.5px solid #e2e8f0",
            borderRadius: "16px", padding: "28px 32px",
            maxWidth: "480px", margin: "0 auto",
            fontFamily: "Segoe UI, Arial, sans-serif",
            boxShadow: "0 4px 20px rgba(0,0,0,0.07)"
        }}>
            <div style={{ marginBottom: "20px" }}>
                <div style={{ fontSize: "18px", fontWeight: 700, color: "#1e293b", marginBottom: "4px" }}>
                    Before we analyze 🩺
                </div>
                <div style={{ fontSize: "13px", color: "#94a3b8" }}>
                    Age and gender help us show accurate normal ranges for your report.
                </div>
            </div>

            {/* Age */}
            <div style={{ marginBottom: "16px" }}>
                <label style={{ fontSize: "12px", fontWeight: 600, color: "#64748b", textTransform: "uppercase", letterSpacing: "0.5px", display: "block", marginBottom: "8px" }}>
                    Age
                </label>
                <input
                    type="number" min="1" max="120"
                    value={age}
                    onChange={e => setAge(e.target.value)}
                    placeholder="Enter your age"
                    style={{
                        width: "100%", padding: "10px 14px",
                        border: "0.5px solid #e2e8f0", borderRadius: "10px",
                        fontSize: "15px", color: "#1e293b", outline: "none",
                        fontFamily: "Segoe UI, Arial, sans-serif"
                    }}
                />
                {age && (
                    <div style={{ fontSize: "11px", color: "#94a3b8", marginTop: "5px" }}>
                        {isChild ? "👶 Pediatric ranges will be used" : isSenior ? "👴 Senior ranges will be used" : "🧑 Adult ranges will be used"}
                    </div>
                )}
            </div>

            {/* Gender */}
            <div style={{ marginBottom: "16px" }}>
                <label style={{ fontSize: "12px", fontWeight: 600, color: "#64748b", textTransform: "uppercase", letterSpacing: "0.5px", display: "block", marginBottom: "8px" }}>
                    Gender
                </label>
                <div style={{ display: "flex", gap: "10px" }}>
                    {["male", "female", "other"].map(g => (
                        <button key={g} onClick={() => setGender(g)} style={{
                            flex: 1, padding: "10px",
                            border: `1.5px solid ${gender === g ? "#3b82f6" : "#e2e8f0"}`,
                            borderRadius: "10px", background: gender === g ? "#eff6ff" : "#fff",
                            color: gender === g ? "#1d4ed8" : "#64748b",
                            fontWeight: gender === g ? 600 : 400,
                            fontSize: "13px", cursor: "pointer",
                            fontFamily: "Segoe UI, Arial, sans-serif",
                            textTransform: "capitalize"
                        }}>
                            {g === "male" ? "♂ Male" : g === "female" ? "♀ Female" : "⚧ Other"}
                        </button>
                    ))}
                </div>
            </div>

            {/* Pregnant — only show for female adults */}
            {gender === "female" && !isChild && (
                <div style={{ marginBottom: "16px" }}>
                    <label style={{ fontSize: "12px", fontWeight: 600, color: "#64748b", textTransform: "uppercase", letterSpacing: "0.5px", display: "block", marginBottom: "8px" }}>
                        Are you pregnant?
                    </label>
                    <div style={{ display: "flex", gap: "10px" }}>
                        {[false, true].map(p => (
                            <button key={String(p)} onClick={() => setPregnant(p)} style={{
                                flex: 1, padding: "10px",
                                border: `1.5px solid ${pregnant === p ? "#3b82f6" : "#e2e8f0"}`,
                                borderRadius: "10px", background: pregnant === p ? "#eff6ff" : "#fff",
                                color: pregnant === p ? "#1d4ed8" : "#64748b",
                                fontWeight: pregnant === p ? 600 : 400,
                                fontSize: "13px", cursor: "pointer",
                                fontFamily: "Segoe UI, Arial, sans-serif"
                            }}>
                                {p ? "Yes" : "No"}
                            </button>
                        ))}
                    </div>
                </div>
            )}

            <button onClick={handleSubmit} style={{
                width: "100%", padding: "13px",
                background: "#3b82f6", color: "white",
                border: "none", borderRadius: "12px",
                fontSize: "15px", fontWeight: 600,
                cursor: "pointer", marginTop: "8px",
                fontFamily: "Segoe UI, Arial, sans-serif"
            }}>
                Continue →
            </button>
        </div>
    );
}

export default UserForm;