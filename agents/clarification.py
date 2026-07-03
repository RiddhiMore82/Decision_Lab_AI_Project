def clarification_agent(state):
    """
    Ask the user for any missing information identified by the Planner.
    """

    answers = {}

    missing = state["planner"].get("missing_information", [])

    # Nothing to ask
    if not missing:
        state["user_context"] = {}
        return state

    print("\n📋 Before the Board meets, I need a little more information.\n")

    for question in missing:

        # Skip empty questions
        if not question.strip():
            continue

        while True:

            answer = input(f"{question}\n> ").strip()

            if answer:
                answers[question] = answer
                break

            print("Please enter a response.")

    state["user_context"] = answers

    return state