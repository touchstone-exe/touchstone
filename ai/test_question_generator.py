from question_generator import generate_skill_questions


# Test 1: Python
result = generate_skill_questions(
    skill="Python",
    claim="Developed a Python automation tool using SQL.",
    evidence="Developed a Python automation tool using SQL."
)

print("\n========== PYTHON ==========")
print(result)

assert result["skill"] == "Python"
assert len(result["questions"]) > 0


# Test 2: FastAPI
result = generate_skill_questions(
    skill="FastAPI",
    claim="Built REST APIs using FastAPI.",
    evidence="Built REST APIs using FastAPI."
)

print("\n========== FASTAPI ==========")
print(result)

assert result["skill"] == "FastAPI"
assert len(result["questions"]) > 0


# Test 3: Unknown skill
result = generate_skill_questions(
    skill="UnknownSkill"
)

print("\n========== UNKNOWN SKILL ==========")
print(result)

assert result["skill"] == "UnknownSkill"
assert result["questions"] == []


print("\n========== QUESTION GENERATOR TEST PASSED ==========")