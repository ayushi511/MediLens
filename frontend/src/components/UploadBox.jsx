import { useDropzone } from "react-dropzone";
import { useState } from "react";
import axios from "axios";
import ResultsList from "./ResultsList";
import UserForm from "./UserForm";
import VerifyValues from "./VerifyValues";

function UploadBox() {
    const [userProfile, setUserProfile]         = useState(null);
    const [fileName, setFileName]               = useState("");
    const [status, setStatus]                   = useState("");
    const [results, setResults]                 = useState([]);
    const [extractedValues, setExtractedValues] = useState([]);
    const [summaryMessage, setSummaryMessage]   = useState("");
    const [stage, setStage]                     = useState("upload");
    const [loading, setLoading]                 = useState(false);

    const onDrop = async (acceptedFiles) => {
        const file = acceptedFiles[0];
        if (!file) return;

        setFileName(file.name);
        setStatus("Extracting values from report...");
        setLoading(true);
        setResults([]);
        setExtractedValues([]);
        setSummaryMessage("");
        setStage("upload");

        const formData = new FormData();
        formData.append("file", file);
        formData.append("age", userProfile.age);
        formData.append("gender", userProfile.gender);
        formData.append("pregnant", userProfile.pregnant);

        try {
            const response = await axios.post(
                "http://127.0.0.1:8000/upload",
                formData,
                { headers: { "Content-Type": "multipart/form-data" } }
            );

            const data = response.data;
            setResults(data.results || []);
            setExtractedValues(data.extracted_values || []);
            setSummaryMessage(data.summary_message || "");

            if ((data.extracted_values || []).length > 0) {
                setStage("verify");
                setStatus("");
            } else if ((data.results || []).length === 0) {
                setStatus("⚠️ No test values could be extracted from this report.");
                setStage("upload");
            } else {
                setStage("results");
                setStatus("✅ Analysis complete!");
            }

        } catch (error) {
            console.error("Upload error:", error);
            setStatus("❌ Upload failed. Is the backend running?");
        } finally {
            setLoading(false);
        }
    };

    const { getRootProps, getInputProps, isDragActive } = useDropzone({
        onDrop,
        accept: { "application/pdf": [".pdf"] },
        multiple: false,
    });

    const StepIndicator = ({ activeStep }) => (
        <div className="ml-steps">
            {[
                { num: 1, label: "Your details" },
                { num: 2, label: "Upload report" },
                { num: 3, label: "View results" },
            ].map((step, i) => (
                <div key={step.num} style={{ display: "flex", alignItems: "center", flex: i < 2 ? 1 : 0 }}>
                    <div className={`ml-step ${activeStep === step.num ? "active" : ""}`}>
                        <div className="ml-step-num">{step.num}</div>
                        {step.label}
                    </div>
                    {i < 2 && <div className="ml-step-line" />}
                </div>
            ))}
        </div>
    );

    // Step 1 — User form
    if (!userProfile) {
        return (
            <div className="ml-form-wrap">
                <StepIndicator activeStep={1} />
                <UserForm onSubmit={setUserProfile} />
            </div>
        );
    }

    return (
        <div>
            <StepIndicator activeStep={
                stage === "results" ? 3 :
                stage === "verify"  ? 3 : 2
            } />

            {/* Profile pill */}
            <div style={{
                display: "flex", alignItems: "center",
                justifyContent: "center", gap: "8px",
                margin: "0 auto 16px"
            }}>
                <span style={{
                    background: "#E6F1FB", color: "#185FA5",
                    padding: "5px 16px", borderRadius: "99px",
                    fontSize: "12px", fontWeight: 600
                }}>
                    <i className="ti ti-user-circle" style={{ marginRight: "5px", fontSize: "13px" }} aria-hidden="true"></i>
                    {userProfile.age} yrs · {userProfile.gender}
                    {userProfile.pregnant ? " · Pregnant" : ""}
                </span>
                <button onClick={() => { setUserProfile(null); setStage("upload"); setResults([]); setFileName(""); }} style={{
                    background: "none", border: "none",
                    color: "#94a3b8", fontSize: "12px",
                    cursor: "pointer", padding: "4px 8px"
                }}>
                    Change
                </button>
            </div>

            {/* Dropzone */}
            <div style={{ maxWidth: "520px", margin: "0 auto", padding: "0 1.5rem" }}>
                <div {...getRootProps()} className={`dropzone ${isDragActive ? "active" : ""}`}>
                    <input {...getInputProps()} />
                    {fileName ? (
                        <div>
                            <i className="ti ti-file-check" style={{ fontSize: "28px", color: "#185FA5", display: "block", marginBottom: "8px" }} aria-hidden="true"></i>
                            <p style={{ margin: 0, fontWeight: 600, color: "#185FA5" }}>{fileName}</p>
                        </div>
                    ) : isDragActive ? (
                        <div>
                            <i className="ti ti-file-upload" style={{ fontSize: "28px", color: "#185FA5", display: "block", marginBottom: "8px" }} aria-hidden="true"></i>
                            <p style={{ margin: 0 }}>Drop your report here...</p>
                        </div>
                    ) : (
                        <div>
                            <i className="ti ti-file-upload" style={{ fontSize: "28px", color: "#85B7EB", display: "block", marginBottom: "8px" }} aria-hidden="true"></i>
                            <p style={{ margin: "0 0 6px", color: "#475569", fontWeight: 500 }}>Drag & drop your PDF report here</p>
                            <p style={{ margin: 0, fontSize: "13px", color: "#94a3b8" }}>or click to browse files</p>
                        </div>
                    )}
                </div>
            </div>

            {loading && <p className="status">⏳ Analyzing... please wait</p>}
            {status && !loading && <p className="status">{status}</p>}

            {/* Step 2 — Verify */}
            {stage === "verify" && extractedValues.length > 0 && (
                <VerifyValues
                    extractedValues={extractedValues}
                    onConfirm={() => setStage("results")}
                />
            )}

            {/* Step 3 — Results */}
            {stage === "results" && (
                <>
                    {summaryMessage && (
                        <div style={{
                            maxWidth: "1000px", margin: "16px auto 0",
                            padding: "12px 20px", background: "#E6F1FB",
                            borderLeft: "4px solid #185FA5",
                            borderRadius: "0 10px 10px 0",
                            fontSize: "13px", color: "#185FA5",
                            fontFamily: "Segoe UI, Arial, sans-serif"
                        }}>
                            ℹ️ {summaryMessage}
                        </div>
                    )}
                    <ResultsList results={results} userProfile={userProfile} />
                </>
            )}

            {/* No results warning */}
            {!loading && stage === "upload" && status.includes("⚠️") && (
                <div style={{
                    maxWidth: "520px", margin: "24px auto",
                    background: "#FFFBEB", border: "1px solid #FDE68A",
                    borderRadius: "14px", padding: "20px 24px",
                    fontFamily: "Segoe UI, Arial, sans-serif"
                }}>
                    <div style={{ fontWeight: 700, color: "#92400E", marginBottom: "8px" }}>
                        ⚠️ No recognisable test values found
                    </div>
                    <div style={{ fontSize: "13px", color: "#78350F", lineHeight: 1.7 }}>
                        This can happen if the PDF is scanned, uses lab-specific abbreviations, or is handwritten. Try uploading a text-based PDF blood test report.
                    </div>
                </div>
            )}
        </div>
    );
}

export default UploadBox;