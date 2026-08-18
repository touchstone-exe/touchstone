QUESTION_BANK = {
    "Python": [
        {
            "question": "Write a Python function that takes a list of integers and returns the sum of all even numbers.",
            "type": "coding"
        },
        {
            "question": "Explain how you would handle an exception when reading a file in Python.",
            "type": "conceptual"
        }
    ],

    "FastAPI": [
        {
            "question": "Create a FastAPI GET endpoint that accepts a name as a query parameter and returns a JSON greeting.",
            "type": "coding"
        },
        {
            "question": "Explain the purpose of Pydantic models in a FastAPI application.",
            "type": "conceptual"
        }
    ],

    "SQL": [
        {
            "question": "Write a SQL query to find all employees whose salary is greater than 50000.",
            "type": "coding"
        },
        {
            "question": "Explain the difference between INNER JOIN and LEFT JOIN.",
            "type": "conceptual"
        }
    ],

    "React": [
        {
            "question": "Create a React component that displays a list of items passed through props.",
            "type": "coding"
        },
        {
            "question": "Explain the purpose of React state and how it differs from props.",
            "type": "conceptual"
        }
    ],

    "JavaScript": [
        {
            "question": "Write a JavaScript function that removes duplicate values from an array.",
            "type": "coding"
        },
        {
            "question": "Explain the difference between let, const, and var.",
            "type": "conceptual"
        }
    ]
}


def generate_skill_questions(
    skill: str,
    claim: str | None = None,
    evidence: str | None = None,
) -> dict:
    """
    Generate skill-specific assessment questions.

    claim and evidence are accepted as context, but this MVP
    does not invent or modify evidence.
    """

    if not isinstance(skill, str):
        raise TypeError("skill must be a string")

    skill = skill.strip()

    if not skill:
        return {
            "skill": "",
            "questions": []
        }

    questions = QUESTION_BANK.get(skill, [])

    return {
        "skill": skill,
        "questions": questions
    }