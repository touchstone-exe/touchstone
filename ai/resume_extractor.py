import re

def _split_resume_into_sentences(resume_text: str) -> list[str]:
    """Split resume text into clean sentence-like chunks."""
    if not resume_text:
        return []

    # Preserve line boundaries from the original resume.
    lines = [
        line.strip()
        for line in resume_text.splitlines()
        if line.strip()
    ]

    chunks = []

    for line in lines:
        # If a line contains multiple sentences, split them.
        sentences = re.split(r"(?<=[.!?])\s+", line)

        for sentence in sentences:
            sentence = sentence.strip()

            if sentence:
                chunks.append(sentence)

    return chunks


def _extract_skills(resume_text: str) -> list[dict]:
    """
    Extract commonly mentioned technical skills from resume text.

    Confidence here means extraction confidence only.
    It does NOT mean the candidate has proven the skill.
    """

    known_skills = {
        "python": "Python",
        "javascript": "JavaScript",
        "typescript": "TypeScript",
        "java": "Java",
        "c++": "C++",
        "c#": "C#",
        "html": "HTML",
        "css": "CSS",
        "react": "React",
        "node.js": "Node.js",
        "nodejs": "Node.js",
        "fastapi": "FastAPI",
        "django": "Django",
        "flask": "Flask",
        "sql": "SQL",
        "mongodb": "MongoDB",
        "postgresql": "PostgreSQL",
        "mysql": "MySQL",
        "git": "Git",
        "github": "GitHub",
        "docker": "Docker",
        "aws": "AWS",
        "machine learning": "Machine Learning",
        "deep learning": "Deep Learning",
        "tensorflow": "TensorFlow",
        "pytorch": "PyTorch",
    }

    lower_text = resume_text.lower()
    found_skills = []
    seen = set()

    for keyword, display_name in known_skills.items():
        pattern = rf"(?<!\w){re.escape(keyword)}(?!\w)"

        if re.search(pattern, lower_text) and display_name not in seen:
            found_skills.append(
                {
                    "name": display_name,
                    "confidence": 0.94,
                }
            )
            seen.add(display_name)

    return found_skills


def _extract_claims_and_evidence(
    resume_text: str,
    skills: list[dict],
) -> tuple[list[dict], list[dict]]:
    """
    Extract simple claims directly from resume sentences.

    Evidence is always copied from the actual resume text.
    No additional evidence is generated.
    """

    sentences = _split_resume_into_sentences(resume_text)

    claims = []
    evidence = []

    skill_lookup = {
        skill["name"].lower(): skill["name"]
        for skill in skills
    }

    # Phrases that commonly indicate a candidate claim/action.
    claim_indicators = (
        "built",
        "developed",
        "created",
        "implemented",
        "designed",
        "worked with",
        "used",
        "using",
        "experience with",
        "experience in",
        "worked on",
        "developed using",
        "built using",
        "implemented using",
    )

    for sentence in sentences:
        lower_sentence = sentence.lower()

        if not any(indicator in lower_sentence for indicator in claim_indicators):
            continue

        matched_skill = None

        for skill_name_lower, display_name in skill_lookup.items():
            pattern = rf"(?<!\w){re.escape(skill_name_lower)}(?!\w)"

            if re.search(pattern, lower_sentence):
                matched_skill = display_name
                break

        if matched_skill is None:
            continue

        claim = {
            "text": sentence,
            "skill": matched_skill,
        }

        claims.append(claim)

        # IMPORTANT:
        # source_text is exactly the sentence from the resume.
        evidence.append(
            {
                "claim": sentence,
                "source_text": sentence,
                "source_type": "resume",
            }
        )

    return claims, evidence


def extract_resume_information(resume_text: str) -> dict:
    """
    Main public function for Resume -> Skills/Claims/Evidence extraction.

    Input:
        resume_text: Raw extracted text from a resume.

    Output:
        {
            "skills": [...],
            "claims": [...],
            "evidence": [...]
        }

    This function does not parse PDF files, call FastAPI,
    access a database, or invent evidence.
    """

    if not isinstance(resume_text, str):
        raise TypeError("resume_text must be a string")

    resume_text = resume_text.strip()

    if not resume_text:
        return {
            "skills": [],
            "claims": [],
            "evidence": [],
        }

    skills = _extract_skills(resume_text)

    claims, evidence = _extract_claims_and_evidence(
        resume_text,
        skills,
    )

    return {
        "skills": skills,
        "claims": claims,
        "evidence": evidence,
    }