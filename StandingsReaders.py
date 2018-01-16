import json
import requests
from collections import defaultdict
from NflSiteStrings import *
class NflWebReader:
    def __init__(self):
        self.url = 'https://www.nfl.com/standings/division/2017/REG'
        self.team_data = {}
        self.team_winning_pcts = {}
        self.team_conferences = {}
        self.division_leaders = defaultdict(list)
    def setTeamData(self):
        error_list = []
        try:
            page = requests.get(self.url)
        except requests.exceptions.RequestException, e:
            error_list.append("Couldn't connect to the page: " + str(e))
        for line in page.content.split("\n"):
            if line.strip().startswith("__INITIAL_DATA__"):
               data_line = line.split("=", 1)[1].strip().strip(";")
               self.team_data = json.loads(data_line)
        if len(self.team_data) == 0:
            error_list.append("Failed to initialize team data")
        return error_list
    def hasPlayed(self, team_name):
        for game in self.team_data['uiState']['scoreStripGames']:
            if game['homeTeam']['identifier'] == team_name or game['awayTeam']['identifier'] == team_name:
                if game['status']['isOver'] == False:
                    return False
        return True
    def populateStandings(self):
        error_list = []
        try:
            for team in self.team_data['instance']['teamRecords']:
                self.team_conferences[team['fullName']] = team[CONFERENCE]
                if team[CONFERENCE] != NFC and team[CONFERENCE] != AFC:
                    error_list.append("Unknown conference: " + team[CONFERENCE])
                self.team_winning_pcts[team['fullName']] = team[WINNING_PCT]
                if team[DIVISION_RANK] == 1:
                    self.division_leaders[team[DIVISION]].append(team['fullName'])
        except KeyError, e:
            error_list.append("Couldn't find expected data on the page. It's likely the page has changed: " + str(e))
        return error_list
