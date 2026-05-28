import ResultCard from "./ResultCard";
import {
  PieChart, Pie, Cell, Tooltip, ResponsiveContainer,
  RadialBarChart, RadialBar,
  LineChart, Line, XAxis, YAxis, CartesianGrid, ReferenceLine,
  BarChart, Bar, LabelList,
} from "recharts";

// ─────────────────────────────────────────────────────────────────────────────
// Helpers
// ─────────────────────────────────────────────────────────────────────────────
const font = "'Segoe UI', system-ui, sans-serif";

function SectionTitle({ children }) {
  return (
    <div style={{
      fontSize: "16px", fontWeight: 700, color: "#0f172a",
      marginBottom: "16px", fontFamily: font,
      display: "flex", alignItems: "center", gap: "8px"
    }}>{children}</div>
  );
}

function ChartCard({ title, children, height = 220 }) {
  return (
    <div style={{
      background: "#fff",
      border: "1px solid #e2e8f0",
      borderRadius: "18px",
      padding: "20px 22px",
      fontFamily: font,
    }}>
      <div style={{ fontSize: "13px", fontWeight: 700, color: "#334155", marginBottom: "16px" }}>
        {title}
      </div>
      <div style={{ height }}>{children}</div>
    </div>
  );
}

// Custom tooltip for line charts
function LineTooltip({ active, payload, label, unit, normalMin, normalMax }) {
  if (!active || !payload?.length) return null;
  const v = payload[0].value;
  const status = v < normalMin ? "Low" : v > normalMax ? "High" : "Normal";
  const statusColor = status === "Normal" ? "#10B981" : status === "Low" ? "#5B8DEF" : "#F43F5E";
  return (
    <div style={{
      background: "#fff", border: "1px solid #e2e8f0",
      borderRadius: "10px", padding: "10px 14px",
      fontSize: "12px", fontFamily: font,
      boxShadow: "0 4px 16px rgba(0,0,0,0.1)"
    }}>
      <div style={{ fontWeight: 700, color: "#0f172a", marginBottom: "4px" }}>{label}</div>
      <div style={{ color: "#64748b" }}>{v} {unit}</div>
      <div style={{ color: statusColor, fontWeight: 600, marginTop: "3px" }}>{status}</div>
    </div>
  );
}

// ─────────────────────────────────────────────────────────────────────────────
// Chart 1 – Blood Sugar Trend  (glucose + hba1c shown together)
// ─────────────────────────────────────────────────────────────────────────────
function SugarTrendChart({ results }) {
  const glucose = results.find(r =>
    r.test?.toLowerCase().includes("glucose") ||
    r.test?.toLowerCase().includes("sugar")
  );
  const hba1c = results.find(r =>
    r.test?.toLowerCase().includes("hba1c") ||
    r.test?.toLowerCase().includes("hb a1c")
  );

  if (!glucose && !hba1c) return null;

  // Build a small simulated-history array for visualization
  // In a real app these would come from historical data
  const buildTrend = (val, min, max) => {
    const spread = (max - min) * 0.3;
    return [
      { month: "3M ago", value: +(val + spread * (Math.random() - 0.5)).toFixed(1) },
      { month: "2M ago", value: +(val + spread * (Math.random() - 0.5)).toFixed(1) },
      { month: "1M ago", value: +(val + spread * (Math.random() - 0.5)).toFixed(1) },
      { month: "Now",    value: val },
    ];
  };

  return (
    <ChartCard title="🍬 Blood Sugar Overview" height={200}>
      <div style={{ display: "grid", gridTemplateColumns: glucose && hba1c ? "1fr 1fr" : "1fr", gap: "16px", height: "100%" }}>
        {glucose && (() => {
          const parts = glucose.normal_range?.split(" - ") || ["70","100"];
          const min = parseFloat(parts[0]), max = parseFloat(parts[1]);
          const data = buildTrend(glucose.value, min, max);
          const color = glucose.status === "NORMAL" ? "#10B981" : glucose.status === "LOW" ? "#5B8DEF" : "#F43F5E";
          return (
            <div>
              <div style={{ fontSize: "11px", color: "#94a3b8", marginBottom: "6px", fontWeight: 600 }}>
                Fasting Blood Sugar &nbsp;
                <span style={{ color, fontWeight: 700 }}>{glucose.value} {glucose.unit}</span>
              </div>
              <ResponsiveContainer width="100%" height={150}>
                <LineChart data={data} margin={{ top: 8, right: 8, left: -20, bottom: 0 }}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#f1f5f9" />
                  <XAxis dataKey="month" tick={{ fontSize: 10, fill: "#94a3b8" }} axisLine={false} tickLine={false} />
                  <YAxis tick={{ fontSize: 10, fill: "#94a3b8" }} axisLine={false} tickLine={false} />
                  <ReferenceLine y={min} stroke="#86EFAC" strokeDasharray="4 3" label={{ value: "Min", fontSize: 9, fill: "#94a3b8" }} />
                  <ReferenceLine y={max} stroke="#FCA5A5" strokeDasharray="4 3" label={{ value: "Max", fontSize: 9, fill: "#94a3b8" }} />
                  <Tooltip content={<LineTooltip unit={glucose.unit} normalMin={min} normalMax={max} />} />
                  <Line type="monotone" dataKey="value" stroke={color} strokeWidth={2.5} dot={{ r: 4, fill: color, stroke: "#fff", strokeWidth: 2 }} activeDot={{ r: 6 }} />
                </LineChart>
              </ResponsiveContainer>
            </div>
          );
        })()}

        {hba1c && (() => {
          const parts = hba1c.normal_range?.split(" - ") || ["4.0","5.6"];
          const min = parseFloat(parts[0]), max = parseFloat(parts[1]);
          const data = buildTrend(hba1c.value, min, max);
          const color = hba1c.status === "NORMAL" ? "#10B981" : hba1c.status === "LOW" ? "#5B8DEF" : "#F43F5E";
          return (
            <div>
              <div style={{ fontSize: "11px", color: "#94a3b8", marginBottom: "6px", fontWeight: 600 }}>
                3-Month Sugar Average (HbA1c) &nbsp;
                <span style={{ color, fontWeight: 700 }}>{hba1c.value} {hba1c.unit}</span>
              </div>
              <ResponsiveContainer width="100%" height={150}>
                <LineChart data={data} margin={{ top: 8, right: 8, left: -20, bottom: 0 }}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#f1f5f9" />
                  <XAxis dataKey="month" tick={{ fontSize: 10, fill: "#94a3b8" }} axisLine={false} tickLine={false} />
                  <YAxis tick={{ fontSize: 10, fill: "#94a3b8" }} axisLine={false} tickLine={false} />
                  <ReferenceLine y={min} stroke="#86EFAC" strokeDasharray="4 3" />
                  <ReferenceLine y={max} stroke="#FCA5A5" strokeDasharray="4 3" />
                  <Tooltip content={<LineTooltip unit={hba1c.unit} normalMin={min} normalMax={max} />} />
                  <Line type="monotone" dataKey="value" stroke={color} strokeWidth={2.5} dot={{ r: 4, fill: color, stroke: "#fff", strokeWidth: 2 }} activeDot={{ r: 6 }} />
                </LineChart>
              </ResponsiveContainer>
            </div>
          );
        })()}
      </div>
    </ChartCard>
  );
}

// ─────────────────────────────────────────────────────────────────────────────
// Chart 2 – Cholesterol & Heart Markers
// ─────────────────────────────────────────────────────────────────────────────
function CholesterolChart({ results }) {
  const chol = results.find(r => r.test?.toLowerCase().includes("cholesterol"));
  if (!chol) return null;

  const parts = chol.normal_range?.split(" - ") || ["0","200"];
  const min = parseFloat(parts[0]), max = parseFloat(parts[1]);
  const color = chol.status === "NORMAL" ? "#10B981" : "#F43F5E";

  const zones = [
    { label: "Ideal\n< 170", range: 170,  fill: "#DCFCE7", textColor: "#166534" },
    { label: "Good\n< 200",  range: 200,  fill: "#D1FAE5", textColor: "#059669" },
    { label: "Border\n200-239", range: 239, fill: "#FEF3C7", textColor: "#92400E" },
    { label: "High\n≥ 240",  range: 280,  fill: "#FFE4E6", textColor: "#9F1239" },
  ];

  // Needle gauge via simple bar
  const pct = Math.min(98, Math.max(2, ((chol.value - 0) / 300) * 100));

  return (
    <ChartCard title="❤️ Heart Fat Level (Cholesterol)" height={180}>
      <div style={{ display: "flex", flexDirection: "column", gap: "14px" }}>
        {/* Zone bar */}
        <div style={{ position: "relative" }}>
          <div style={{ display: "flex", height: "28px", borderRadius: "8px", overflow: "hidden" }}>
            {zones.map((z, i) => (
              <div key={i} style={{ flex: 1, background: z.fill, display: "flex", alignItems: "center", justifyContent: "center" }}>
                <span style={{ fontSize: "9px", fontWeight: 700, color: z.textColor, whiteSpace: "pre", textAlign: "center", lineHeight: 1.3 }}>
                  {z.label}
                </span>
              </div>
            ))}
          </div>
          {/* Pointer */}
          <div style={{
            position: "absolute", bottom: "-6px",
            left: `${pct}%`, transform: "translateX(-50%)",
            width: 0, height: 0,
            borderLeft: "6px solid transparent",
            borderRight: "6px solid transparent",
            borderTop: `10px solid ${color}`
          }} />
        </div>

        {/* Value display */}
        <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", paddingTop: "10px" }}>
          <div>
            <span style={{ fontSize: "42px", fontWeight: 800, color: "#0f172a", lineHeight: 1 }}>{chol.value}</span>
            <span style={{ fontSize: "14px", color: "#94a3b8", marginLeft: "6px" }}>mg/dL</span>
          </div>
          <div style={{ textAlign: "right" }}>
            <div style={{
              fontSize: "13px", fontWeight: 700, color: color,
              background: chol.status === "NORMAL" ? "#DCFCE7" : "#FFE4E6",
              padding: "5px 14px", borderRadius: "99px"
            }}>
              {chol.status === "NORMAL" ? "✅ Healthy range" : "⚠ Above ideal"}
            </div>
            <div style={{ fontSize: "11px", color: "#94a3b8", marginTop: "5px" }}>Ideal: below 200 mg/dL</div>
          </div>
        </div>

        {/* Simple tip */}
        <div style={{ fontSize: "12px", color: "#64748b", background: "#f8fafc", borderRadius: "8px", padding: "8px 12px" }}>
          💡 Total cholesterol below 200 mg/dL is considered heart-healthy. Above 240 mg/dL needs medical attention.
        </div>
      </div>
    </ChartCard>
  );
}

// ─────────────────────────────────────────────────────────────────────────────
// Chart 3 – CBC (Complete Blood Count) Visual
// ─────────────────────────────────────────────────────────────────────────────
function CBCChart({ results }) {
  const CBC_KEYS = ["hemoglobin", "rbc", "wbc", "platelets"];
  const FRIENDLY = {
    hemoglobin: "Hemoglobin",
    rbc:        "Red Cells",
    wbc:        "White Cells",
    platelets:  "Platelets",
  };

  const cbcResults = results.filter(r => {
    const t = r.test?.toLowerCase().replace(/\s/g, "_");
    return CBC_KEYS.some(k => t?.includes(k.replace("_", "")) || t === k);
  });

  if (cbcResults.length === 0) return null;

  const data = cbcResults.map(r => {
    const parts = r.normal_range?.split(" - ") || ["0","100"];
    const min = parseFloat(parts[0]), max = parseFloat(parts[1]);
    // Normalise to 0-100% scale within range (50 = dead center normal)
    const mid = (min + max) / 2;
    const range = max - min;
    const pct = Math.min(100, Math.max(0, 50 + ((r.value - mid) / range) * 100));
    const color = r.status === "NORMAL" ? "#10B981"
                : r.status === "LOW"    ? "#5B8DEF"
                : r.status.includes("CRITICAL") ? "#DC2626"
                : "#F43F5E";
    const label = FRIENDLY[r.test?.toLowerCase().replace(/\s/g, "_")] || r.test;
    return { name: label, pct: +pct.toFixed(1), color, status: r.status, value: r.value, unit: r.unit };
  });

  const CustomBarLabel = ({ x, y, width, value, index }) => {
    const d = data[index];
    return (
      <text x={x + width + 8} y={y + 12} fill={d.color} fontSize={11} fontWeight={700}>
        {d.value} {d.unit}
      </text>
    );
  };

  return (
    <ChartCard title="🩸 Blood Count Overview (CBC)" height={data.length * 52 + 20}>
      <ResponsiveContainer width="100%" height="100%">
        <BarChart
          data={data}
          layout="vertical"
          margin={{ top: 4, right: 90, left: 10, bottom: 4 }}
          barCategoryGap="30%"
        >
          <CartesianGrid horizontal={false} stroke="#f1f5f9" />
          <XAxis type="number" domain={[0, 100]} hide />
          <YAxis
            type="category" dataKey="name"
            tick={{ fontSize: 12, fill: "#334155", fontWeight: 600 }}
            axisLine={false} tickLine={false} width={80}
          />
          {/* Normal band */}
          <ReferenceLine x={30} stroke="#e2e8f0" strokeDasharray="3 3" />
          <ReferenceLine x={70} stroke="#e2e8f0" strokeDasharray="3 3" />
          {/* Green band background via rect - approximated via two reference areas */}
          <Tooltip
            formatter={(v, _, props) => [`${props.payload.value} ${props.payload.unit}`, props.payload.name]}
          />
          <Bar dataKey="pct" radius={[0, 6, 6, 0]} minPointSize={4}>
            {data.map((d, i) => <Cell key={i} fill={d.color} fillOpacity={0.85} />)}
            <LabelList content={<CustomBarLabel />} />
          </Bar>
        </BarChart>
      </ResponsiveContainer>
      {/* Legend */}
      <div style={{ display: "flex", gap: "14px", justifyContent: "center", marginTop: "6px", fontSize: "11px", color: "#64748b" }}>
        {[["#10B981","Normal"],["#5B8DEF","Low"],["#F43F5E","High"],["#DC2626","Critical"]].map(([c,l]) => (
          <span key={l} style={{ display: "flex", alignItems: "center", gap: "5px" }}>
            <span style={{ width: 10, height: 10, borderRadius: 3, background: c, display: "inline-block" }} />
            {l}
          </span>
        ))}
      </div>
      <div style={{ fontSize: "11px", color: "#94a3b8", textAlign: "center", marginTop: "6px" }}>
        Bar position shows where your value sits between Low ← → High
      </div>
    </ChartCard>
  );
}

// ─────────────────────────────────────────────────────────────────────────────
// Chart 4 – Deficiency Indicators (vitamins, minerals, electrolytes)
// ─────────────────────────────────────────────────────────────────────────────
function DeficiencyChart({ results }) {
  const DEF_KEYS   = ["vitamin", "calcium", "sodium", "potassium", "iron", "ferritin", "zinc", "magnesium", "b12", "folate"];
  const ICON_MAP   = { vitamin_d: "☀️", calcium: "🦴", sodium: "⚡", potassium: "🍌", b12: "💊", iron: "⚙️" };

  const defResults = results.filter(r => {
    const t = r.test?.toLowerCase().replace(/\s/g, "_");
    return DEF_KEYS.some(k => t?.includes(k));
  });
  if (defResults.length === 0) return null;

  const statusLabel = s => s === "NORMAL" ? "Sufficient" : s === "LOW" ? "Deficient" : s === "HIGH" ? "Excess" : s;
  const statusColor = s => s === "NORMAL" ? "#10B981" : s === "LOW" ? "#F59E0B" : "#F43F5E";
  const statusBg    = s => s === "NORMAL" ? "#DCFCE7" : s === "LOW" ? "#FEF3C7" : "#FFE4E6";

  return (
    <ChartCard title="💊 Vitamins & Minerals Status" height={defResults.length * 58 + 16}>
      <div style={{ display: "flex", flexDirection: "column", gap: "10px" }}>
        {defResults.map((r, i) => {
          const parts = r.normal_range?.split(" - ") || ["0","100"];
          const min = parseFloat(parts[0]), max = parseFloat(parts[1]);
          const pct = isNaN(min)||isNaN(max) ? 50
            : Math.min(96, Math.max(4, ((r.value - min) / (max - min)) * 100));
          const color = statusColor(r.status);
          const key   = r.test?.toLowerCase().replace(/\s/g, "_");
          const icon  = Object.entries(ICON_MAP).find(([k]) => key?.includes(k))?.[1] || "💊";

          return (
            <div key={i} style={{
              display: "grid",
              gridTemplateColumns: "28px 1fr 90px",
              alignItems: "center",
              gap: "10px",
              padding: "8px 10px",
              background: "#f8fafc",
              borderRadius: "12px",
            }}>
              <span style={{ fontSize: "18px", textAlign: "center" }}>{icon}</span>
              <div>
                <div style={{ fontSize: "12px", fontWeight: 600, color: "#334155", marginBottom: "5px" }}>
                  {r.test}
                  <span style={{ fontSize: "10px", color: "#94a3b8", marginLeft: "6px" }}>
                    {r.value} {r.unit}
                  </span>
                </div>
                {/* Mini bar */}
                <div style={{ position: "relative" }}>
                  <div style={{ display: "flex", height: "7px", gap: "3px" }}>
                    <div style={{ flex: 2, background: "#93C5FD", borderRadius: "3px" }} />
                    <div style={{ flex: 3, background: "#86EFAC", borderRadius: "3px" }} />
                    <div style={{ flex: 2, background: "#FCA5A5", borderRadius: "3px" }} />
                  </div>
                  <div style={{
                    position: "absolute", top: "50%",
                    left: `${pct}%`,
                    transform: "translate(-50%, -50%)",
                    width: "12px", height: "12px",
                    borderRadius: "50%", background: color,
                    border: "2px solid white",
                    boxShadow: "0 1px 4px rgba(0,0,0,0.2)"
                  }} />
                </div>
              </div>
              <span style={{
                fontSize: "11px", fontWeight: 700,
                padding: "4px 10px", borderRadius: "99px",
                background: statusBg(r.status),
                color: statusColor(r.status),
                textAlign: "center"
              }}>
                {statusLabel(r.status)}
              </span>
            </div>
          );
        })}
      </div>
    </ChartCard>
  );
}

// ─────────────────────────────────────────────────────────────────────────────
// Main ResultsList
// ─────────────────────────────────────────────────────────────────────────────
function ResultsList({ results }) {
  if (!results || results.length === 0) return null;

  const normal   = results.filter(r => r.status === "NORMAL").length;
  const abnormal = results.filter(r => r.status === "LOW" || r.status === "HIGH").length;
  const critical = results.filter(r => r.status.includes("CRITICAL")).length;
  const total    = results.length;
  const score    = Math.round((normal / total) * 100);
  const scoreColor = score >= 75 ? "#10B981" : score >= 50 ? "#F59E0B" : "#F43F5E";

  const pieData = [
    { name: "Normal",   value: normal,   color: "#10B981" },
    { name: "Abnormal", value: abnormal, color: "#F59E0B" },
    { name: "Critical", value: critical, color: "#F43F5E" },
  ].filter(d => d.value > 0);

  const gaugeData = [{ value: score, fill: scoreColor }];

  // Check which charts are relevant
  const hasSugar      = results.some(r => ["glucose","hba1c","sugar"].some(k => r.test?.toLowerCase().includes(k)));
  const hasCholesterol = results.some(r => r.test?.toLowerCase().includes("cholesterol"));
  const hasCBC        = results.some(r => ["hemoglobin","rbc","wbc","platelets"].some(k => r.test?.toLowerCase().includes(k)));
  const hasDeficiency = results.some(r => ["vitamin","calcium","sodium","potassium"].some(k => r.test?.toLowerCase().includes(k)));
  const showCharts    = hasSugar || hasCholesterol || hasCBC || hasDeficiency;

  return (
    <div style={{ maxWidth: "1100px", margin: "0 auto", padding: "20px 24px 56px", fontFamily: font }}>

      {/* Critical banner */}
      {critical > 0 && (
        <div style={{
          background: "#FFF1F2", borderLeft: "5px solid #F43F5E",
          color: "#9F1239", padding: "14px 20px", borderRadius: "12px",
          fontWeight: 600, fontSize: "14px", marginBottom: "24px",
          textAlign: "justify"
        }}>
          🚨 {critical} critical value{critical > 1 ? "s" : ""} detected — please consult a doctor as soon as possible.
        </div>
      )}

      {/* ── Dashboard row ── */}
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: "16px", marginBottom: "32px" }}>

        {/* Health score */}
        <div style={{ background: "#fff", border: "1px solid #e2e8f0", borderRadius: "18px", padding: "20px", textAlign: "center" }}>
          <div style={{ fontSize: "11px", color: "#94a3b8", textTransform: "uppercase", letterSpacing: "0.6px", marginBottom: "8px", fontWeight: 700 }}>
            Health Score
          </div>
          <ResponsiveContainer width="100%" height={130}>
            <RadialBarChart innerRadius="60%" outerRadius="100%" data={gaugeData} startAngle={180} endAngle={0}>
              <RadialBar dataKey="value" max={100} cornerRadius={6} />
            </RadialBarChart>
          </ResponsiveContainer>
          <div style={{ fontSize: "32px", fontWeight: 800, color: scoreColor, marginTop: "-6px" }}>
            {score}%
          </div>
          <div style={{ fontSize: "12px", color: "#94a3b8", marginTop: "3px" }}>
            {score >= 75 ? "Looking good!" : score >= 50 ? "Needs attention" : "Consult a doctor"}
          </div>
        </div>

        {/* Donut */}
        <div style={{ background: "#fff", border: "1px solid #e2e8f0", borderRadius: "18px", padding: "20px", textAlign: "center" }}>
          <div style={{ fontSize: "11px", color: "#94a3b8", textTransform: "uppercase", letterSpacing: "0.6px", marginBottom: "8px", fontWeight: 700 }}>
            Result Breakdown
          </div>
          <ResponsiveContainer width="100%" height={130}>
            <PieChart>
              <Pie data={pieData} cx="50%" cy="50%" innerRadius={38} outerRadius={62} dataKey="value" paddingAngle={3}>
                {pieData.map((e, i) => <Cell key={i} fill={e.color} />)}
              </Pie>
              <Tooltip formatter={(v, n) => [v, n]} />
            </PieChart>
          </ResponsiveContainer>
          <div style={{ display: "flex", justifyContent: "center", gap: "10px", flexWrap: "wrap", fontSize: "11px", color: "#64748b", marginTop: "6px" }}>
            {pieData.map((d, i) => (
              <span key={i} style={{ display: "flex", alignItems: "center", gap: "4px" }}>
                <span style={{ width: "9px", height: "9px", borderRadius: "2px", background: d.color, display: "inline-block" }} />
                {d.name}: {d.value}
              </span>
            ))}
          </div>
        </div>

        {/* Summary */}
        <div style={{ background: "#fff", border: "1px solid #e2e8f0", borderRadius: "18px", padding: "20px" }}>
          <div style={{ fontSize: "11px", color: "#94a3b8", textTransform: "uppercase", letterSpacing: "0.6px", marginBottom: "14px", fontWeight: 700, textAlign: "center" }}>
            Summary
          </div>
          {[
            { label: "✅ Normal",   num: normal,   bg: "#DCFCE7", color: "#166534" },
            { label: "⚠ Abnormal", num: abnormal, bg: "#FEF3C7", color: "#92400E" },
            { label: "🚨 Critical", num: critical, bg: "#FFE4E6", color: "#9F1239" },
            { label: "📋 Total",    num: total,    bg: "#EFF6FF", color: "#1E40AF" },
          ].map((s, i) => (
            <div key={i} style={{
              display: "flex", alignItems: "center", justifyContent: "space-between",
              padding: "8px 14px", borderRadius: "10px", marginBottom: "8px",
              background: s.bg, color: s.color, fontWeight: 500, fontSize: "13px"
            }}>
              <span>{s.label}</span>
              <span style={{ fontSize: "22px", fontWeight: 800 }}>{s.num}</span>
            </div>
          ))}
        </div>
      </div>

      {/* ── Charts section ── */}
      {showCharts && (
        <>
          <SectionTitle>📊 Health Charts</SectionTitle>
          <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(460px, 1fr))", gap: "16px", marginBottom: "36px" }}>
            {hasSugar       && <SugarTrendChart   results={results} />}
            {hasCholesterol && <CholesterolChart  results={results} />}
            {hasCBC         && <CBCChart          results={results} />}
            {hasDeficiency  && <DeficiencyChart   results={results} />}
          </div>
        </>
      )}

      {/* ── Individual cards ── */}
      <SectionTitle>📋 All Test Results</SectionTitle>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(300px, 1fr))", gap: "16px" }}>
        {results.map((result, i) => <ResultCard key={i} result={result} />)}
      </div>
    </div>
  );
}

export default ResultsList;
