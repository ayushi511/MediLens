import "../styles/home.css";
import UploadBox from "../components/UploadBox";

function Home() {
    return (
        <div className="ml-page">

            {/* Nav */}
            <nav className="ml-nav">
                <div className="ml-logo">
                    <div className="ml-logo-icon">
                        <i className="ti ti-heart-rate-monitor" aria-hidden="true"></i>
                    </div>
                    <span className="ml-logo-text"><span>Medi</span>Lens</span>
                </div>
                <span className="ml-nav-tag">
                    <i className="ti ti-shield-check" aria-hidden="true"></i> Awareness tool only
                </span>
            </nav>

            {/* Hero */}
            <div className="ml-hero">
                <div className="ml-hero-badge">
                    <i className="ti ti-sparkles" aria-hidden="true"></i>
                    Understand your reports in plain language
                </div>
                <h1 className="ml-hero-title">
                    Talk to your <span>report</span>
                </h1>
                <p className="ml-hero-sub">
                    Upload your blood test report and get a clear, simple breakdown — no medical degree required.
                </p>
            </div>

            {/* Upload box */}
            <UploadBox />

            {/* Features */}
            <div className="ml-features">
                <div className="ml-feat">
                    <div className="ml-feat-icon blue">
                        <i className="ti ti-eye" aria-hidden="true"></i>
                    </div>
                    <h3>Plain language</h3>
                    <p>No jargon. Every result explained simply.</p>
                </div>
                <div className="ml-feat">
                    <div className="ml-feat-icon green">
                        <i className="ti ti-chart-bar" aria-hidden="true"></i>
                    </div>
                    <h3>Visual charts</h3>
                    <p>See where your values stand at a glance.</p>
                </div>
                <div className="ml-feat">
                    <div className="ml-feat-icon amber">
                        <i className="ti ti-user-check" aria-hidden="true"></i>
                    </div>
                    <h3>Age-aware ranges</h3>
                    <p>Ranges adjust for your age and gender.</p>
                </div>
                <div className="ml-feat">
                    <div className="ml-feat-icon purple">
                        <i className="ti ti-shield-check" aria-hidden="true"></i>
                    </div>
                    <h3>Verify before analysis</h3>
                    <p>You confirm values before we analyze.</p>
                </div>
                <div className="ml-feat">
                    <div className="ml-feat-icon teal">
                        <i className="ti ti-stethoscope" aria-hidden="true"></i>
                    </div>
                    <h3>Doctor guidance</h3>
                    <p>Know exactly when to see a doctor.</p>
                </div>
                <div className="ml-feat">
                    <div className="ml-feat-icon red">
                        <i className="ti ti-alert-triangle" aria-hidden="true"></i>
                    </div>
                    <h3>Critical alerts</h3>
                    <p>Urgent values flagged immediately.</p>
                </div>
            </div>

            {/* Disclaimer */}
            <p className="ml-disclaimer">
                MediLens is an awareness tool only. It does not diagnose, treat, or replace professional medical advice. Always consult your doctor.
            </p>

        </div>
    );
}

export default Home;