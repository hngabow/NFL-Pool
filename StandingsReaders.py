import json
import requests 
from collections import defaultdict
from NflSiteStrings import *
class NflWebReader:
    def __init__(self):
        self.url = 'https://www.nfl.com/standings'
        self.team_data = {}
        self.team_winning_pcts = {}
        self.team_conferences = {}
        self.division_leaders = defaultdict(list)
    def setTeamData(self):
        page = requests.get(self.url)
        for line in page.content.split("\n"):
           if line.strip().startswith("__INITIAL_DATA__"):
               data_line = line.split("=", 1)[1].strip().strip(";")
               self.team_data = json.loads(data_line)
    def hasPlayed(self, team_name):
        for game in self.team_data['uiState']['scoreStripGames']:
            if game['homeTeam']['identifier'] == team_name or game['awayTeam']['identifier'] == team_name:
                if game['status']['isOver'] == False:
                    return False
        return True
    def populateStandings(self):
        for team in self.team_data['instance']['teamRecords']:
            self.team_conferences[team['fullName']] = team[CONFERENCE]
            self.team_winning_pcts[team['fullName']] = team[WINNING_PCT]
            if team[DIVISION_RANK] == 1:
                self.division_leaders[team[DIVISION]].append(team['fullName'])
