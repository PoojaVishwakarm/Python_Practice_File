
import datetime

class Player:
    def __init__(self, fname, lname, bdate, team):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = bdate
        self.team = team

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year

class TennisPlayer(Player):
    def __init__(self, fname, lname, bdate, team):
        super().__init__(fname, lname, bdate, team)

roger = TennisPlayer('Pooja', 'Vishwakarma', 2000, 'India')

print(roger.first_name)
print("Age:", roger.get_age())
