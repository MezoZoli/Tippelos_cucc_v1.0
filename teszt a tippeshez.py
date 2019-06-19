def evaluate_v01(home_goals, away_goals, home_guess, away_guess):
    evaluate = home_goals + away_goals
    guesses = home_guess + away_guess
    home_goals = home_goals
    home_guess = home_guess
    away_goals = away_goals
    away_guess = away_guess
    points = 25
    min_points = 17
    if evaluate == guesses and home_goals == home_guess and away_goals == away_guess:
        points = points
        print(points)

    elif home_goals != home_guess or away_goals != away_guess:
        points = points-25
        print(points)

    elif evaluate == guesses +-1:
        points = points-5
        print(points)

# ha a tipp több lett:

    elif evaluate == guesses + 1:
        min_points = min_points - 2
        print(min_points)
    elif evaluate == guesses + 2:
        min_points = min_points - 4
        print(min_points)
    elif evaluate == guesses + 3:
        min_points = min_points - 6
        print(min_points)
    elif evaluate == guesses + 4:
        min_points = min_points - 8
        print(min_points)
    elif evaluate == guesses + 5:
        min_points = min_points - 10
        print(min_points)
    elif evaluate == guesses + 6:
        min_points = min_points - 12
        print(min_points)
    elif evaluate == guesses + 7:
        min_points = min_points - 14
        print(min_points)
    elif evaluate == guesses + 8:
        min_points = min_points - 16
        print(min_points)
    elif evaluate == guesses + 9:
        min_points = min_points - 18
        print(min_points)
    elif evaluate == guesses + 10:
        min_points = min_points - 20
        print(min_points)
    elif evaluate == guesses + 11:
        min_points = min_points - 22
        print(min_points)
    elif evaluate == guesses + 12:
        min_points = min_points - 24
        print(min_points)

    # ha a tipp kevesebb lett:

    elif evaluate == guesses - 1:
        min_points = min_points - 2
        print(min_points)
    elif evaluate == guesses - 2:
        min_points = min_points - 4
        print(min_points)
    elif evaluate == guesses - 3:
        min_points = min_points - 6
        print(min_points)
    elif evaluate == guesses - 4:
        min_points = min_points - 8
        print(min_points)
    elif evaluate == guesses - 5:
        min_points = min_points - 10
        print(min_points)
    elif evaluate == guesses - 6:
        min_points = min_points - 12
        print(min_points)
    elif evaluate == guesses - 7:
        min_points = min_points - 14
        print(min_points)
    elif evaluate == guesses - 8:
        min_points = min_points - 16
        print(min_points)
    elif evaluate == guesses - 9:
        min_points = min_points - 18
        print(min_points)
    elif evaluate == guesses - 10:
        min_points = min_points - 20
        print(min_points)
    elif evaluate == guesses - 11:
        min_points = min_points - 22
        print(min_points)
    elif evaluate == guesses - 12:
        min_points = min_points - 24
        print(min_points)


evaluate_v01(6, 3, 4, 2)
