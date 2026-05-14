def calculate_result(questions, answers):

    scores = {

        "visual": 0,

        "auditory": 0,

        "kinesthetic": 0

    }

    for q in questions:

        answer = answers.get(q['id'])

        if answer:

            scores[answer] += 1

    total = sum(scores.values())

    percentages = {

        key: round(
            (value / total) * 100,
            2
        )

        for key, value in scores.items()

    }

    dominant = max(
        scores,
        key=scores.get
    )

    return dominant, percentages