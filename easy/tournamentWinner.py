def tournamentWinner(competitions, results):
    i = 0
    best_team = ''
    scores = {best_team: 0}
    for comp in competitions:
        if results[i] == 0:
            winner = comp[1]
        else:
            winner = comp[0]
        if winner in scores:
            scores[winner] = scores[winner] + 3
        else:
            scores[winner] = 3
        if scores[winner] > scores[best_team]:
            best_team = winner
        i = i + 1
    return best_team


competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
]
results = [0, 0, 1]

sol = tournamentWinner(competitions, results)
print(sol)
