class CricketPlayer:
    team_size = 11

    def __init__(self, fname, lname, bdate, team):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = bdate
        self.team = team
        self.scores = []

    def add_scoro(self, score): 
        self.scores.append(score)

    def get_average_score(self):
        return sum(self.scores) / len(self.scores)


virat = CricketPlayer('Pooja', 'Vishwakarma', 35, 'India')
virat.add_scoro(37)
virat.add_scoro(90)
virat.add_scoro(78)

print(virat.team)
print(virat.first_name)
print(virat.last_name)
print(virat.birth_year)
print("Average Score:", virat.get_average_score())
