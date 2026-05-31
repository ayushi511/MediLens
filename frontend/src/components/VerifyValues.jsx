import { useState } from "react";

function VerifyValues({ extractedValues, onConfirm, onEdit }) {
    const [values, setValues] = useState(extractedValues);

    const updateValue = (index, newVal) => {
        const updated = [...values];
        updated[index] = { ...updated[index], value: parseFloat(newVal) || 0 };
        setValues(updated);
    };

    return (
        <div style={{
            maxWidth: "600px", margin: "20px auto",
            background: "#fff", borderRadius: "16px",
            border: "0.5px solid #e2e8f0", padding: "24px",
            fontFamily: "Segoe UI, Arial, sans-serif"
        }}>
            <div style={{ marginBottom: "20px" }}>
                <div style={{ fontSize: "17px", fontWeight: 700, color: "#1e293b", marginBottom: "4px" }}>
                    ✅ Verify Extracted Values
                </div>
                <div style={{ fontSize: "13px", color: "#94a3b8" }}>
                    Please check these values match your report. Correct any errors before analysis.
                </div>
            </div>

            <div style={{ display: "flex", flexDirection: "column", gap: "10px", marginBottom: "20px" }}>
                {values.map((v, i) => (
                    <div key={i} style={{
                        display: "flex", alignItems: "center",
                        justifyContent: "space-between",
                        padding: "10px 14px", background: "#f8fafc",
                        borderRadius: "10px", gap: "12px"
                    }}>
                        <div style={{ flex: 1 }}>
                            <div style={{ fontSize: "13px", fontWeight: 600, color: "#1e293b" }}>{v.test}</div>
                            {v.was_converted && (
                                <div style={{ fontSize: "11px", color: "#94a3b8", marginTop: "2px" }}>
                                    Converted: {v.original_value} {v.original_unit} → {v.converted_unit}
                                </div>
                            )}
                        </div>
                        <div style={{ display: "flex", alignItems: "center", gap: "6px" }}>
                            <input
                                type="number"
                                value={v.value}
                                onChange={e => updateValue(i, e.target.value)}
                                style={{
                                    width: "80px", padding: "6px 10px",
                                    border: "0.5px solid #e2e8f0",
                                    borderRadius: "8px", fontSize: "14px",
                                    fontWeight: 600, color: "#1e293b",
                                    textAlign: "right", outline: "none"
                                }}
                            />
                            <span style={{ fontSize: "12px", color: "#94a3b8", minWidth: "50px" }}>
                                {v.unit}
                            </span>
                        </div>
                    </div>
                ))}
            </div>

            {/* Warning */}
            <div style={{
                background: "#FFFBEB", borderRadius: "10px",
                padding: "10px 14px", fontSize: "12px",
                color: "#92400e", marginBottom: "16px",
                border: "0.5px solid #FDE68A"
            }}>
                ⚠️ Please verify each value against your original report before analysis.
Scanned or image-based PDFs may have extraction errors — this is normal
and expected. Simply correct any wrong values above.
            </div>

            <button onClick={() => onConfirm(values)} style={{
                width: "100%", padding: "12px",
                background: "#3b82f6", color: "white",
                border: "none", borderRadius: "12px",
                fontSize: "15px", fontWeight: 600,
                cursor: "pointer", fontFamily: "Segoe UI, Arial, sans-serif"
            }}>
                Looks correct — Analyze now →
            </button>
        </div>
    );
}

export default VerifyValues;