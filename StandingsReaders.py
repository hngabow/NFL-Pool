import json
import requests 
from NflSiteStrings import *
class NflWebReader:
    def __init__(self):
        self.url = 'https://www.nfl.com/standings'
        self.team_data = {}
        self.afc_standings = {}
        self.nfc_standings = {}
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
            if team[CONFERENCE] == NFC:
                self.nfc_standings[team['fullName']] = (team[WINNING_PCT])
            elif team[CONFERENCE] == AFC:
                self.afc_standings[team['fullName']] = (team[WINNING_PCT])
            else:
                raise Exception("Could not determine conference, data likely changed")
