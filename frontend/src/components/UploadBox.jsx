import { useDropzone } from "react-dropzone";
import { useState } from "react";
import axios from "axios";
import ResultsList from "./ResultsList";

function UploadBox() {
    const [fileName, setFileName] = useState("");
    const [status, setStatus] = useState("");
    const [results, setResults] = useState([]);
    const [loading, setLoading] = useState(false);
    const [debugText, setDebugText] = useState("");

    const onDrop = async (acceptedFiles) => {
        const file = acceptedFiles[0];
        if (!file) return;

        setFileName(file.name);
        setStatus("Analyzing your report...");
        setLoading(true);
        setResults([]);

        const formData = new FormData();
        formData.append("file", file);

        try {
            const response = await axios.post(
                "http://127.0.0.1:8000/upload",
                formData,
                { headers: { "Content-Type": "multipart/form-data" } }
            );
            setStatus("✅ Analysis complete!");
            setResults(response.data.results);
            setDebugText(response.data.debug_text || "");
        } catch (error) {
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

    return (
        <div>
            <div {...getRootProps()} className={`dropzone ${isDragActive ? "active" : ""}`}>
                <input {...getInputProps()} />
                {fileName ? (
                    <p>📄 {fileName}</p>
                ) : isDragActive ? (
                    <p>Drop your report here...</p>
                ) : (
                    <p>Drag & drop a medical report here, or click to select</p>
                )}
            </div>

            {status && <p className="status">{status}</p>}
            {loading && <p className="status">⏳ Please wait...</p>}

            <ResultsList results={results} />
        </div>
    );
}

export default UploadBox;