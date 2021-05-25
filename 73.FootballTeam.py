##this program is going to show the league table from a Brazilian championship
# the 5 first team
# the 4 last placed , the alphabetical order and the position of Sao Paulo

teams = ('Flamengo', 'Palmeiras', 'Gremio', 'International', 'Athetico', 'Santos', 'Corinthians',
          'Sao Paulo', 'Atletico', 'Cruzeiro',
         'Bahia', 'Fluminence', 'Botafogo', 'Ceara',
         'Chapecoense', 'Vasco', 'America', 'Fortaleza', 'Atletico Goa', 'Sport')
print('-' * 20)
print(f'The five first teams in the league table are {teams[0:5]}')
print('-' * 20)
print(f'The four last teams in the league table are{teams[-4:]}')
print('-' * 20)
print(f'the league table in a alphabetical order is {sorted(teams)}')
print('-' * 20)
print('The position of Sao Paulo in the league table is {}'.format(teams.index("Sao Paulo")+1))
print('-'*20)
