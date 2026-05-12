def calculate_result(questions, form_data):

    scores = {
        "visual": 0,
        "auditory": 0,
        "kinesthetic": 0
    }

    for q in questions:

        answer = int(form_data.get(str(q["id"]), 0))

        final_score = answer * q["weight"]

        scores[q["type"]] += final_score

    total = sum(scores.values())

    percentages = {}

    for key, value in scores.items():

        if total == 0:
            percentages[key] = 0
        else:
            percentages[key] = round((value / total) * 100, 2)

    dominant = max(percentages, key=percentages.get)

    return dominant, percentages