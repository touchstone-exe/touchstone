from resume_extractor import extract_resume_information


resume_text = """
Rahul Sharma

Skills:
Python, FastAPI, SQL, React

Projects:
Built REST APIs using FastAPI.
Developed a Python automation tool using SQL.
Created a React dashboard for project analytics.

Education:
B.Tech Computer Science
""" 


result = extract_resume_information(resume_text)

print("\n========== SKILLS ==========")
for skill in result["skills"]:
    print(skill)

print("\n========== CLAIMS ==========")
for claim in result["claims"]:
    print(claim)

print("\n========== EVIDENCE ==========")
for evidence in result["evidence"]:
    print(evidence)


# Basic validation
assert isinstance(result, dict)

assert "skills" in result
assert "claims" in result
assert "evidence" in result

# Skills should be detected
skill_names = [skill["name"] for skill in result["skills"]]

assert "Python" in skill_names
assert "FastAPI" in skill_names
assert "SQL" in skill_names
assert "React" in skill_names

# Evidence must come from the original resume
for item in result["evidence"]:
    assert item["source_type"] == "resume"
    assert item["source_text"] in resume_text

print("\n========== TEST PASSED ==========")