def evaluate_v01(home_goals, away_goals, home_guess, away_guess):
    evaluate = home_goals + away_goals
    guesses = home_guess + away_guess
    points = 25
    min_points = 17
    med_points = 20

    if evaluate == guesses and home_goals == home_guess and away_goals == away_guess:
        points = points
        return points

    elif evaluate == guesses -1:
        points = 20
        return points

    elif evaluate == guesses +1:
        points = 20
        return points

    # GÓLHIBÁK
    # ha a tipp több lett:

    if evaluate == guesses + 1:
        min_points = min_points - 3
        return min_points
    elif evaluate == guesses + 2:
        min_points = min_points - 6
        return min_points
    elif evaluate == guesses + 3:
        min_points = min_points - 9
        return min_points
    elif evaluate == guesses + 4:
        min_points = min_points - 12
        return min_points
    elif evaluate == guesses + 5:
        min_points = min_points - 15
        return min_points
    elif evaluate == guesses + 6:
        min_points = 0
        return min_points

    # ha a tipp kevesebb lett:

    elif evaluate == guesses - 1:
        min_points = min_points - 3
        return min_points
    elif evaluate == guesses - 2:
        min_points = min_points - 6
        return min_points
    elif evaluate == guesses - 3:
        min_points = min_points - 9
        return min_points
    elif evaluate == guesses - 4:
        min_points = min_points - 12
        return min_points
    elif evaluate == guesses - 5:
        min_points = min_points - 15
        return min_points
    elif evaluate == guesses - 6:
        min_points = 0
        return min_points

    # GÓLKÜLÖMBSÉG HIBÁI
    # Ha többre tippel

    if home_goals + 1 and away_goals + 1 == home_guess and away_guess:
        med_points = med_points
        return med_points
    elif home_goals + 2 and away_goals + 2 == home_guess and away_guess:
        med_points = med_points - 2
        return med_points
    elif home_goals + 3 and away_goals + 3 == home_guess and away_guess:
        med_points = med_points - 4
        return med_points
    elif home_goals + 4 and away_goals + 4 == home_guess and away_guess:
        med_points = med_points - 6
        return med_points
    elif home_goals + 5 and away_goals + 5 == home_guess and away_guess:
        med_points = med_points - 8
        return med_points
    elif home_goals + 6 and away_goals + 6 == home_guess and away_guess:
        med_points = med_points - 10
        return med_points
    elif home_goals + 7 and away_goals + 7 == home_guess and away_guess:
        med_points = med_points - 12
        return med_points
    elif home_goals + 8 and away_goals + 8 == home_guess and away_guess:
        med_points = med_points - 14
        return med_points
    elif home_goals + 9 and away_goals + 9 == home_guess and away_guess:
        med_points = med_points - 16
        return med_points
    elif home_goals + 10 and away_goals + 10 == home_guess and away_guess:
        med_points = med_points - 18
        return med_points
    elif home_goals + 11 and away_goals + 11 == home_guess and away_guess:
        med_points = 0
        return med_points

    # Ha kevesebbre tippel

    if home_goals - 1 and away_goals - 1 == home_guess and away_guess:
        med_points = med_points
        return med_points
    elif home_goals - 2 and away_goals - 2 == home_guess and away_guess:
        med_points = med_points - 2
        return med_points
    elif home_goals - 3 and away_goals - 3 == home_guess and away_guess:
        med_points = med_points - 4
        return med_points
    elif home_goals - 4 and away_goals - 4 == home_guess and away_guess:
        med_points = med_points - 6
        return med_points
    elif home_goals - 5 and away_goals - 5 == home_guess and away_guess:
        med_points = med_points - 8
        return med_points
    elif home_goals - 6 and away_goals - 6 == home_guess and away_guess:
        med_points = med_points - 10
        return med_points
    elif home_goals - 7 and away_goals - 7 == home_guess and away_guess:
        med_points = med_points - 12
        return med_points
    elif home_goals - 8 and away_goals - 8 == home_guess and away_guess:
        med_points = med_points - 14
        return med_points
    elif home_goals - 9 and away_goals - 9 == home_guess and away_guess:
        med_points = med_points - 16
        return med_points
    elif home_goals - 10 and away_goals - 10 == home_guess and away_guess:
        med_points = med_points - 18
        return med_points
    elif home_goals - 11 and away_goals - 11 == home_guess and away_guess:
        med_points = 0
        return med_points

    elif home_goals != home_guess or away_goals != away_guess:
        points = 0
        return points


print(evaluate_v01(3, 3, 2, 2))
