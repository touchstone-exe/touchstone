from task_generator import generate_real_world_task


# Test 1: Python
result = generate_real_world_task(
    skill="Python",
    claim="Developed a Python automation tool using SQL.",
    evidence="Developed a Python automation tool using SQL.",
)

print("\n========== PYTHON TASK ==========")
print(result)

assert result["skill"] == "Python"
assert result["task"] is not None
assert result["task"]["skill"] == "Python"


# Test 2: FastAPI
result = generate_real_world_task(
    skill="FastAPI",
    claim="Built REST APIs using FastAPI.",
    evidence="Built REST APIs using FastAPI.",
)

print("\n========== FASTAPI TASK ==========")
print(result)

assert result["skill"] == "FastAPI"
assert result["task"] is not None


# Test 3: Unknown skill
result = generate_real_world_task(
    skill="UnknownSkill"
)

print("\n========== UNKNOWN SKILL ==========")
print(result)

assert result["skill"] == "UnknownSkill"
assert result["task"] is None


print("\n========== TASK GENERATOR TEST PASSED ==========")