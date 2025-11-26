import datetime

def get_average_score(player):
    return sum(player['scores'])/len(player['scores'])

def get_age(player):
    curecnt_year=datetime.datetime.now().year
    return curecnt_year-player['birth_year']

virat={
    'first_name':'virat',
    'last_name':'kohali',
    'scores':[],
    'birth_date':1988
    }

virat['scores'].append(88)
virat['scores'].append(90)
virat['scores'].append(70)

print(get_average_score(virat))