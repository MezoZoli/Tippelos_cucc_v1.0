def evaluate_v01(home_goals, away_goals, home_guess, away_guess):
    evaluate = home_goals + away_goals
    guesses = home_guess + away_guess
    points = 25
    if evaluate == guesses:
        points = points
        print(points)

# ha a tipp több lett:

    elif evaluate == guesses + 1:
        points = points-3
        print(points)
    elif evaluate == guesses + 2:
        points = points-6
        print(points)
    elif evaluate == guesses + 3:
        points = points-9
        print(points)
    elif evaluate == guesses + 4:
        points = points-12
        print(points)
    elif evaluate == guesses + 5:
        points = points-15
        print(points)
    elif evaluate == guesses + 6:
        points = points-18
        print(points)
    elif evaluate == guesses + 7:
        points = points-21
        print(points)
    elif evaluate == guesses + 8:
        points = points-24
        print(points)
    elif evaluate == guesses + 9:
        points = points-25
        print(points)

# ha a tipp kevesebb lett:

    elif evaluate == guesses - 1:
        points = points - 3
        print(points)
    elif evaluate == guesses - 2:
        points = points - 6
        print(points)
    elif evaluate == guesses - 3:
        points = points - 9
        print(points)
    elif evaluate == guesses - 4:
        points = points - 12
        print(points)
    elif evaluate == guesses - 5:
        points = points - 15
        print(points)
    elif evaluate == guesses - 6:
        points = points - 18
        print(points)
    elif evaluate == guesses - 7:
        points = points - 21
        print(points)
    elif evaluate == guesses - 8:
        points = points - 24
        print(points)
    elif evaluate == guesses - 9:
        points = points - 25
        print(points)


evaluate_v01(6, 3, 4, 2)
