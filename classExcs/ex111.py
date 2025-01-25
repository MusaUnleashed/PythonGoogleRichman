import requests
from pprint import pprint

url = "https://gist.githubusercontent.com/nonZero/b86339d7d97417fff297/raw/e30f0a6b3e62f7707240e03893379f0c97f5b2e9/worldcup.json"

res = requests.get(url).json()

for team in res:
    homeTeam = team["home_team"]["country"]
    awayTeam = team["away_team"]["country"]
    awayGoal = team["home_team"]["goals"]
    homeGoal = team["home_team"]["goals"]
    print(f" {homeTeam} - {awayTeam}: {homeGoal}-{awayGoal}")
