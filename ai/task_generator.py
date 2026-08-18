TASK_BANK = {
    "Python": {
        "title": "Python Data Processing Task",
        "description": (
            "Write a Python function that takes a list of transaction "
            "amounts and returns the total of all positive amounts."
        ),
        "skill": "Python",
        "type": "coding",
    },

    "FastAPI": {
        "title": "FastAPI Endpoint Task",
        "description": (
            "Create a FastAPI GET endpoint at /users/{user_id} "
            "that returns the user ID as JSON."
        ),
        "skill": "FastAPI",
        "type": "coding",
    },

    "SQL": {
        "title": "SQL Query Task",
        "description": (
            "Write a SQL query that returns employees whose salary "
            "is greater than 50000."
        ),
        "skill": "SQL",
        "type": "coding",
    },

    "React": {
        "title": "React Component Task",
        "description": (
            "Create a React component that receives a list of items "
            "through props and displays them as a list."
        ),
        "skill": "React",
        "type": "coding",
    },

    "JavaScript": {
        "title": "JavaScript Array Task",
        "description": (
            "Write a JavaScript function that removes duplicate "
            "values from an array."
        ),
        "skill": "JavaScript",
        "type": "coding",
    },
}


def generate_real_world_task(
    skill: str,
    claim: str | None = None,
    evidence: str | None = None,
) -> dict:
    """
    Generate a practical task for a detected skill.

    claim and evidence are accepted as context for future
    AI-based task generation. This MVP does not invent
    or modify candidate evidence.
    """

    if not isinstance(skill, str):
        raise TypeError("skill must be a string")

    skill = skill.strip()

    if not skill:
        return {
            "skill": "",
            "task": None,
        }

    task = TASK_BANK.get(skill)

    if task is None:
        return {
            "skill": skill,
            "task": None,
        }

    return {
        "skill": skill,
        "task": task,
    }