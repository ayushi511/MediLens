import "../styles/home.css";
import UploadBox from "../components/UploadBox";

function Home() {
    return (
        <div className="home-container">
            <h1 className="title">Talk To Your Reports</h1>
            <p className="subtitle">
                Understand medical reports in plain English
            </p>
            <UploadBox />
        </div>
    );
}

export default Home;