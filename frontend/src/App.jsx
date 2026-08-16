import { useState } from "react";
import "./App.css";

function App() {
  const [page, setPage] = useState("home");

  const startVerification = () => {
    setPage("upload");
  };

  return (
    <div className="app">

      <nav className="navbar">
        <div className="logo">TouchStone</div>
        <div className="nav-tag">Skills × Evidence × Proof</div>
      </nav>

      {page === "home" && (
        <main className="hero">
          <p className="eyebrow">THE PROOF-FIRST TALENT PLATFORM</p>

          <h1>
            Don't just say
            <br />
            <span>you're skilled.</span>
            <br />
            Prove it.
          </h1>

          <p className="subtitle">
            Turn your claimed skills into verifiable proof using real
            evidence and practical challenges.
          </p>

          <button className="primary-btn" onClick={startVerification}>
            Verify My Skills →
          </button>

          <div className="trust-row">
            <span>✓ Evidence-backed</span>
            <span>✓ Practical assessment</span>
            <span>✓ Verifiable proof</span>
          </div>
        </main>
      )}

      {page === "upload" && (
        <main className="page">
          <p className="eyebrow">STEP 01 — CLAIMS</p>

          <h2>Let's see what you claim.</h2>

          <p className="page-subtitle">
            Upload your resume. TouchStone will identify the skills you claim
            and prepare them for verification.
          </p>

          <div className="upload-box">
            <div className="upload-icon">↑</div>

            <h3>Drop your resume here</h3>

            <p>PDF only • Max 10MB</p>

            <label className="upload-btn">
              Choose Resume
              <input type="file" accept=".pdf" hidden />
            </label>
          </div>

          <div className="demo-note">
            <strong>Demo mode</strong>
            <br />
            For this prototype, resume processing will use sample candidate
            data. The final system will extract claims automatically.
          </div>

          <button
            className="secondary-btn"
            onClick={() => setPage("claims")}
          >
            Continue Demo →
          </button>
        </main>
      )}

      {page === "claims" && (
        <main className="page">
          <p className="eyebrow">STEP 02 — DETECTED CLAIMS</p>

          <h2>Here's what we found.</h2>

          <p className="page-subtitle">
            TouchStone detected these skills from the candidate's resume.
          </p>

          <div className="claims">

            <div className="claim-card selected">
              <div>
                <h3>Python</h3>
                <p>Claimed level: Intermediate</p>
              </div>
              <span>Selected</span>
            </div>

            <div className="claim-card">
              <div>
                <h3>Data Analysis</h3>
                <p>Claimed level: Intermediate</p>
              </div>
              <span>Detected</span>
            </div>

            <div className="claim-card">
              <div>
                <h3>Machine Learning</h3>
                <p>Claimed level: Beginner</p>
              </div>
              <span>Detected</span>
            </div>

          </div>

          <button
            className="primary-btn"
            onClick={() => setPage("evidence")}
          >
            Prove Python →
          </button>
        </main>
      )}

      {page === "evidence" && (
        <main className="page">
          <p className="eyebrow">STEP 03 — EVIDENCE</p>

          <h2>Now let's check the proof.</h2>

          <p className="page-subtitle">
            Claims aren't enough. TouchStone looks for evidence that supports
            them.
          </p>

          <div className="evidence-box">
            <div className="github-row">
              <div>
                <h3>GitHub</h3>
                <p>Connect your public GitHub profile</p>
              </div>

              <button className="connect-btn">
                Connect
              </button>
            </div>

            <div className="evidence-result">
              <div>
                <span>Repositories</span>
                <strong>4 relevant</strong>
              </div>

              <div>
                <span>Python usage</span>
                <strong>High</strong>
              </div>

              <div>
                <span>Project evidence</span>
                <strong>4 sources</strong>
              </div>
            </div>
          </div>

          <button
            className="primary-btn"
            onClick={() => setPage("challenge")}
          >
            Start Proof Challenge →
          </button>
        </main>
      )}

      {page === "challenge" && (
        <main className="page challenge-page">
          <div className="challenge-header">
            <div>
              <p className="eyebrow">STEP 04 — PROOF CHALLENGE</p>
              <h2>Python · Intermediate</h2>
            </div>

            <div className="timer">03:00</div>
          </div>

          <div className="challenge-box">

            <p className="question-label">REAL-WORLD TASK</p>

            <h3>
              Your team receives 500,000 transaction records.
              The current Python solution takes 18 seconds to process them.
              How would you redesign it to make it significantly faster?
            </h3>

            <p className="question-hint">
              Explain your approach and show a practical implementation.
            </p>

            <textarea
              placeholder="Explain your approach..."
              rows="8"
            />

            <div className="integrity">
              🔒 Assessment integrity monitoring active
            </div>

            <button
              className="primary-btn"
              onClick={() => setPage("result")}
            >
              Submit Challenge →
            </button>

          </div>
        </main>
      )}

      {page === "result" && (
        <main className="page">
          <p className="eyebrow">STEP 05 — VERIFICATION RESULT</p>

          <h2>Your skill has been tested.</h2>

          <div className="score-card">

            <div className="score-top">
              <div>
                <p>Python</p>
                <h3>Intermediate</h3>
              </div>

              <div className="score">
                87<span>/100</span>
              </div>
            </div>

            <div className="metrics">

              <div>
                <span>Approach</span>
                <strong>23/25</strong>
              </div>

              <div>
                <span>Correctness</span>
                <strong>24/25</strong>
              </div>

              <div>
                <span>Reasoning</span>
                <strong>17/20</strong>
              </div>

              <div>
                <span>Code Quality</span>
                <strong>9/10</strong>
              </div>

            </div>

            <div className="verification-summary">
              <p>✓ Evidence matched</p>
              <p>✓ Practical proof passed</p>
              <p>✓ No integrity violations detected</p>
            </div>

          </div>

          <button
            className="primary-btn"
            onClick={() => setPage("proof")}
          >
            Generate Proof Card →
          </button>
        </main>
      )}

      {page === "proof" && (
        <main className="page">
          <p className="eyebrow">VERIFIED BY TOUCHSTONE</p>

          <h2>Proof, not promises.</h2>

          <div className="proof-card">

            <div className="proof-header">
              <div>
                <p>TOUCHSTONE PROOF</p>
                <h3>Python</h3>
              </div>

              <div className="verified">
                ✓ VERIFIED
              </div>
            </div>

            <div className="proof-score">
              <span>Confidence</span>
              <strong>87%</strong>
            </div>

            <div className="proof-details">
              <div>
                <span>Claim</span>
                <strong>Intermediate</strong>
              </div>

              <div>
                <span>Evidence</span>
                <strong>4 sources</strong>
              </div>

              <div>
                <span>Practical proof</span>
                <strong>Passed</strong>
              </div>

              <div>
                <span>Integrity</span>
                <strong>Verified</strong>
              </div>
            </div>

            <div className="proof-id">
              Proof ID: TS-8F29-K4A1
            </div>

            <div className="fingerprint">
              SHA-256: 8f29c4...a81d
            </div>

          </div>

          <button
            className="secondary-btn"
            onClick={() => setPage("home")}
          >
            Back to TouchStone
          </button>

        </main>
      )}

    </div>
  );
}

export default App;