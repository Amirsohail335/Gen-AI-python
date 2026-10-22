# print("I am learning AI engineering.")
# print("Python is my foundation.")
print("I will build, test, and explain real systems.")


def multiply(a: int, b: int) -> int:
    return a * b

print(multiply("ha", 3))



attempt = 0

while attempt < 3:
    print("Attempt:", attempt + 1)
    attempt += 1


def analyze_skills(
    required_skills: list[str],
    existing_skills: list[str],
) -> dict[str, list[str]]:
    existing = {
        skill.strip().casefold()
        for skill in existing_skills
        if skill.strip()
    }

    matched = []
    missing = []

    for skill in required_skills:
        normalized = skill.strip().casefold()

        if normalized in existing:
            matched.append(skill)
        else:
            missing.append(skill)

    return {
        "matched": matched,
        "missing": missing,
    }


def main() -> None:
    required = [
        "Python",
        "FastAPI",
        "RAG",
        "LangGraph",
        "SQL",
    ]

    existing = [
        "python",
        "FastAPI",
        "React",
        "Node.js",
    ]

    result = analyze_skills(required, existing)

    print("Matched:", result["matched"])
    print("Missing:", result["missing"])
    print("Matched count:", len(result["matched"]))


if __name__ == "__main__":
    main()
