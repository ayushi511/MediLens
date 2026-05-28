import { useState } from "react";

// ── plain-English label map ──────────────────────────────────────────────────
const FRIENDLY_NAMES = {
  "Serum Creatinine":           "Kidney Health Marker",
  "Creatinine":                 "Kidney Health Marker",
  "HbA1c":                      "3-Month Sugar Average",
  "Hemoglobin":                 "Oxygen Carrier (Hemoglobin)",
  "WBC":                        "Infection Fighter (WBC)",
  "RBC":                        "Red Blood Cells",
  "Platelets":                  "Clotting Cells (Platelets)",
  "Glucose":                    "Blood Sugar Level",
  "Cholesterol":                "Heart Fat Level",
  "TSH":                        "Thyroid Activity",
  "Uric Acid":                  "Joint Health Marker",
  "Sodium":                     "Salt Balance (Sodium)",
  "Potassium":                  "Heart Mineral (Potassium)",
  "Bilirubin":                  "Liver Waste Marker",
  "SGPT":                       "Liver Enzyme (SGPT)",
  "SGOT":                       "Liver Enzyme (SGOT)",
  "Vitamin D":                  "Bone Vitamin (D)",
  "Calcium":                    "Bone Mineral (Calcium)",
};

function friendlyName(raw) {
  return FRIENDLY_NAMES[raw] || raw;
}

// ── Small segmented bar used inside the modal ────────────────────────────────
function ScaleBar({ pct, color, size = "modal" }) {
  const h  = size === "card" ? "8px"  : "11px";
  const dh = size === "card" ? "14px" : "18px";
  const dw = size === "card" ? "14px" : "18px";
  return (
    <div>
      <div style={{ position: "relative", marginBottom: "6px" }}>
        <div style={{ display: "flex", height: h, gap: "4px" }}>
          <div style={{ flex: 2, background: "#93C5FD", borderRadius: "4px" }} />
          <div style={{ flex: 3, background: "#86EFAC", borderRadius: "4px" }} />
          <div style={{ flex: 2, background: "#FCA5A5", borderRadius: "4px" }} />
        </div>
        <div style={{
          position: "absolute", top: "50%",
          left: `${pct}%`,
          transform: "translate(-50%, -50%)",
          width: dw, height: dh,
          borderRadius: "50%", background: color,
          border: "3px solid white",
          boxShadow: "0 2px 8px rgba(0,0,0,0.22)"
        }} />
      </div>
      <div style={{ display: "flex", justifyContent: "space-between", fontSize: "10px", color: "#94a3b8" }}>
        <span>Low</span><span>Normal</span><span>High</span>
      </div>
    </div>
  );
}

// ── Section heading inside modal ─────────────────────────────────────────────
function SectionLabel({ children }) {
  return (
    <div style={{
      fontSize: "10px", fontWeight: 700, color: "#94a3b8",
      textTransform: "uppercase", letterSpacing: "0.8px",
      marginBottom: "10px"
    }}>{children}</div>
  );
}

// ── Pill chip ────────────────────────────────────────────────────────────────
function Chip({ children, bg, color }) {
  return (
    <span style={{
      padding: "7px 15px", borderRadius: "99px",
      fontSize: "13px", fontWeight: 500,
      background: bg, color,
      lineHeight: 1.4,
      display: "inline-block"
    }}>{children}</span>
  );
}

// ── Modal ────────────────────────────────────────────────────────────────────
function Modal({ result, cfg, onClose }) {
  const parts = result.normal_range?.split(" - ") || [];
  const min   = parseFloat(parts[0]);
  const max   = parseFloat(parts[1]);
  const pct   = isNaN(min) || isNaN(max) ? 50
    : Math.min(96, Math.max(4, ((result.value - min) / (max - min)) * 100));

  const font = "Georgia, 'Times New Roman', serif";
  const body = "'Segoe UI', system-ui, sans-serif";

  return (
    <>
      {/* Backdrop */}
      <div onClick={onClose} style={{
        position: "fixed", inset: 0,
        background: "rgba(15,23,42,0.5)",
        zIndex: 200, backdropFilter: "blur(6px)"
      }} />

      {/* Panel */}
      <div style={{
        position: "fixed", top: "50%", left: "50%",
        transform: "translate(-50%, -50%)",
        width: "660px", maxWidth: "95vw",
        maxHeight: "90vh", overflowY: "auto",
        background: "#fff", borderRadius: "24px",
        zIndex: 201,
        boxShadow: "0 40px 100px rgba(0,0,0,0.28)",
        fontFamily: body,
        animation: "popIn 0.22s cubic-bezier(.34,1.56,.64,1)"
      }}>
        <style>{`
          @keyframes popIn {
            from { transform: translate(-50%,-44%); opacity:0; }
            to   { transform: translate(-50%,-50%); opacity:1; }
          }
          .modal-scroll::-webkit-scrollbar { width: 5px; }
          .modal-scroll::-webkit-scrollbar-track { background: transparent; }
          .modal-scroll::-webkit-scrollbar-thumb { background: #e2e8f0; border-radius: 99px; }
        `}</style>

        {/* Top accent strip */}
        <div style={{ height: "6px", background: cfg.color, borderRadius: "24px 24px 0 0" }} />

        {/* ── Header ── */}
        <div style={{
          padding: "22px 28px 18px",
          borderBottom: "1px solid #f1f5f9",
          display: "flex", alignItems: "center", gap: "16px"
        }}>
          <div style={{
            width: "56px", height: "56px", borderRadius: "16px",
            background: cfg.iconBg, display: "flex",
            alignItems: "center", justifyContent: "center",
            fontSize: "28px", flexShrink: 0
          }}>{result.emoji}</div>

          <div style={{ flex: 1, minWidth: 0 }}>
            <div style={{ fontSize: "20px", fontWeight: 700, color: "#0f172a", fontFamily: font }}>
              {friendlyName(result.test)}
            </div>
            {friendlyName(result.test) !== result.test && (
              <div style={{ fontSize: "11px", color: "#94a3b8", marginTop: "2px" }}>
                Medical name: {result.test}
              </div>
            )}
            <div style={{ fontSize: "11px", color: "#94a3b8", textTransform: "uppercase", letterSpacing: "0.5px", marginTop: "3px" }}>
              {result.category}
            </div>
          </div>

          <span style={{
            fontSize: "12px", fontWeight: 700, padding: "5px 16px",
            borderRadius: "99px", background: cfg.badgeBg, color: cfg.badgeText,
            flexShrink: 0
          }}>{cfg.label}</span>

          <button onClick={onClose} style={{
            width: "34px", height: "34px", borderRadius: "10px",
            border: "none", background: "#f1f5f9", cursor: "pointer",
            fontSize: "16px", color: "#64748b",
            display: "flex", alignItems: "center", justifyContent: "center",
            flexShrink: 0, fontFamily: body
          }}>✕</button>
        </div>

        {/* ── Body ── */}
        <div className="modal-scroll" style={{
          padding: "24px 28px",
          display: "flex", flexDirection: "column", gap: "22px"
        }}>

          {/* Value card */}
          <div style={{
            background: cfg.iconBg, borderRadius: "16px",
            padding: "18px 22px",
            display: "flex", alignItems: "flex-end", justifyContent: "space-between"
          }}>
            <div>
              <div style={{ fontSize: "52px", fontWeight: 800, color: "#0f172a", lineHeight: 1, fontFamily: font }}>
                {result.value}
                <span style={{ fontSize: "17px", fontWeight: 400, color: "#94a3b8", marginLeft: "8px", fontFamily: body }}>
                  {result.unit}
                </span>
              </div>
              <div style={{ fontSize: "12px", color: "#94a3b8", marginTop: "6px" }}>
                Healthy range: {result.normal_range} {result.unit}
              </div>
            </div>
            <div style={{
              fontSize: "13px", fontWeight: 600, color: cfg.badgeText,
              background: cfg.badgeBg, padding: "6px 16px", borderRadius: "99px"
            }}>
              {result.status === "NORMAL" ? "✅ You're good!" :
               result.status === "LOW"    ? "⬇ Below normal" :
               result.status === "HIGH"   ? "⬆ Above normal" : "⚠ Check urgently"}
            </div>
          </div>

          {/* Scale bar */}
          <ScaleBar pct={pct} color={cfg.color} size="modal" />

          {/* Critical alert */}
          {result.status.includes("CRITICAL") && (
            <div style={{
              background: "#FFF1F2", color: "#9F1239",
              fontSize: "14px", fontWeight: 600,
              padding: "14px 18px", borderRadius: "12px",
              border: "1px solid #FECDD3",
              textAlign: "justify"
            }}>
              🚨 This value is critically outside the safe range. Please see a doctor as soon as possible.
            </div>
          )}

          {/* Message */}
          {result.status !== "NORMAL" && result.message && (
            <div style={{
              borderLeft: `4px solid ${cfg.color}`,
              background: cfg.iconBg,
              padding: "14px 18px",
              borderRadius: "0 12px 12px 0",
              fontSize: "14px", color: "#334155",
              lineHeight: 1.75,
              textAlign: "justify"
            }}>
              {result.message}
            </div>
          )}

          {/* What this means */}
          {result.what_it_means?.length > 0 && (
            <div>
              <SectionLabel>🔍 What this means for you</SectionLabel>
              <div style={{ display: "flex", flexDirection: "column", gap: "8px" }}>
                {result.what_it_means.map((item, i) => (
                  <div key={i} style={{
                    fontSize: "13.5px", color: "#334155",
                    padding: "10px 16px",
                    background: "#f8fafc",
                    borderRadius: "10px",
                    lineHeight: 1.7,
                    textAlign: "justify",
                    borderLeft: `3px solid ${cfg.color}`
                  }}>
                    {item}
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Eat & Avoid side-by-side */}
          {(result.eat?.length > 0 || result.avoid?.length > 0) && (
            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "16px" }}>
              {result.eat?.length > 0 && (
                <div>
                  <SectionLabel>✅ Eat more of</SectionLabel>
                  <div style={{ display: "flex", flexWrap: "wrap", gap: "7px" }}>
                    {result.eat.map((item, i) => (
                      <Chip key={i} bg="#DCFCE7" color="#166534">{item}</Chip>
                    ))}
                  </div>
                </div>
              )}
              {result.avoid?.length > 0 && (
                <div>
                  <SectionLabel>❌ Avoid these</SectionLabel>
                  <div style={{ display: "flex", flexWrap: "wrap", gap: "7px" }}>
                    {result.avoid.map((item, i) => (
                      <Chip key={i} bg="#FFE4E6" color="#9F1239">{item}</Chip>
                    ))}
                  </div>
                </div>
              )}
            </div>
          )}

          {/* Tips */}
          {result.tips?.length > 0 && (
            <div>
              <SectionLabel>💡 Simple tips to improve</SectionLabel>
              <div style={{ display: "flex", flexWrap: "wrap", gap: "8px" }}>
                {result.tips.map((item, i) => (
                  <Chip key={i} bg="#DBEAFE" color="#1E40AF">{item}</Chip>
                ))}
              </div>
            </div>
          )}

          {/* See doctor if */}
          {result.see_doctor_if?.length > 0 && (
            <div style={{ background: "#FFFBEB", borderRadius: "14px", padding: "18px 20px" }}>
              <div style={{ fontSize: "14px", fontWeight: 700, color: "#92400e", marginBottom: "12px" }}>
                🩺 Go to a doctor if you notice…
              </div>
              {result.see_doctor_if.map((s, i) => (
                <div key={i} style={{
                  fontSize: "13.5px", color: "#78350f",
                  padding: "6px 0",
                  lineHeight: 1.7,
                  textAlign: "justify",
                  borderBottom: i < result.see_doctor_if.length - 1 ? "1px solid #FDE68A" : "none"
                }}>
                  • {s}
                </div>
              ))}
            </div>
          )}

          {/* Did you know */}
          {result.did_you_know && (
            <div style={{
              background: "#EFF6FF", borderRadius: "14px",
              padding: "16px 20px",
              fontSize: "13.5px", color: "#1E40AF",
              fontStyle: "italic", lineHeight: 1.75,
              textAlign: "justify"
            }}>
              💡 <strong>Did you know?</strong> {result.did_you_know}
            </div>
          )}

          {/* Related tests */}
          {result.related_tests?.length > 0 && (
            <div style={{ fontSize: "12px", color: "#94a3b8" }}>
              🔗 Related tests: {result.related_tests.join(", ")}
            </div>
          )}

          {/* Disclaimer */}
          <p style={{
            fontSize: "10.5px", color: "#cbd5e1",
            fontStyle: "italic", margin: 0,
            textAlign: "justify", lineHeight: 1.7
          }}>
            {result.medical_disclaimer}
          </p>
        </div>
      </div>
    </>
  );
}

// ── Result Card ──────────────────────────────────────────────────────────────
function ResultCard({ result }) {
  const [open, setOpen] = useState(false);

  const statusMap = {
    "NORMAL":        { color: "#10B981", iconBg: "#ECFDF5", badgeBg: "#DCFCE7", badgeText: "#166534", label: "Normal"   },
    "LOW":           { color: "#5B8DEF", iconBg: "#EEF3FE", badgeBg: "#FEF3C7", badgeText: "#92400E", label: "Low"      },
    "HIGH":          { color: "#F43F5E", iconBg: "#FFF1F2", badgeBg: "#FFE4E6", badgeText: "#9F1239", label: "High"     },
    "CRITICAL LOW":  { color: "#DC2626", iconBg: "#FFF1F2", badgeBg: "#FFE4E6", badgeText: "#7F1D1D", label: "Critical" },
    "CRITICAL HIGH": { color: "#DC2626", iconBg: "#FFF1F2", badgeBg: "#FFE4E6", badgeText: "#7F1D1D", label: "Critical" },
  };
  const cfg = statusMap[result.status] || {
    color: "#94a3b8", iconBg: "#f1f5f9",
    badgeBg: "#f1f5f9", badgeText: "#475569", label: result.status
  };

  const parts = result.normal_range?.split(" - ") || [];
  const min   = parseFloat(parts[0]);
  const max   = parseFloat(parts[1]);
  const pct   = isNaN(min) || isNaN(max) ? 50
    : Math.min(96, Math.max(4, ((result.value - min) / (max - min)) * 100));

  return (
    <>
      {open && <Modal result={result} cfg={cfg} onClose={() => setOpen(false)} />}

      <div
        onClick={() => setOpen(true)}
        style={{
          background: "#fff",
          border: "1px solid #e2e8f0",
          borderRadius: "18px", overflow: "hidden",
          cursor: "pointer",
          fontFamily: "'Segoe UI', system-ui, sans-serif",
          transition: "transform 0.15s, box-shadow 0.15s",
        }}
        onMouseEnter={e => {
          e.currentTarget.style.transform = "translateY(-3px)";
          e.currentTarget.style.boxShadow = "0 10px 32px rgba(0,0,0,0.11)";
        }}
        onMouseLeave={e => {
          e.currentTarget.style.transform = "translateY(0)";
          e.currentTarget.style.boxShadow = "none";
        }}
      >
        <div style={{ height: "5px", background: cfg.color }} />

        <div style={{ padding: "16px 18px" }}>
          {/* Header row */}
          <div style={{ display: "flex", alignItems: "center", gap: "10px", marginBottom: "14px" }}>
            <div style={{
              width: "42px", height: "42px", borderRadius: "12px",
              background: cfg.iconBg, display: "flex",
              alignItems: "center", justifyContent: "center",
              fontSize: "20px", flexShrink: 0
            }}>{result.emoji}</div>
            <div style={{ flex: 1, minWidth: 0 }}>
              <div style={{ fontSize: "14px", fontWeight: 600, color: "#0f172a", whiteSpace: "nowrap", overflow: "hidden", textOverflow: "ellipsis" }}>
                {friendlyName(result.test)}
              </div>
              <div style={{ fontSize: "10px", color: "#94a3b8", textTransform: "uppercase", letterSpacing: "0.4px", marginTop: "2px" }}>
                {result.category}
              </div>
            </div>
            <span style={{
              fontSize: "10px", fontWeight: 700, padding: "3px 10px",
              borderRadius: "99px", background: cfg.badgeBg, color: cfg.badgeText,
              flexShrink: 0
            }}>{cfg.label}</span>
          </div>

          {/* Value */}
          <div style={{ marginBottom: "4px" }}>
            <span style={{ fontSize: "36px", fontWeight: 800, color: "#0f172a", lineHeight: 1 }}>{result.value}</span>
            <span style={{ fontSize: "12px", color: "#94a3b8", marginLeft: "6px" }}>{result.unit}</span>
          </div>
          <div style={{ fontSize: "11px", color: "#94a3b8", marginBottom: "12px" }}>
            Normal: {result.normal_range}
          </div>

          {/* Bar */}
          <ScaleBar pct={pct} color={cfg.color} size="card" />

          <div style={{ fontSize: "10px", color: "#cbd5e1", textAlign: "right", marginTop: "10px" }}>
            Tap for details →
          </div>
        </div>
      </div>
    </>
  );
}

export default ResultCard;
