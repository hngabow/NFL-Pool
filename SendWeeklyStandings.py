from PicksReaders import PicksFileReader, PicksStub
from ContestantsNotifier import SpyNotifier 
from StandingsReaders import NflWebReader
from TeamInfo import TeamInfo
from NflSiteStrings import AFC, NFC
class SendWeeklyStandings(object):
    def __init__(self, picks_reader, notifier, standings_reader):
        self.picks = picks_reader
        self.notifier = notifier
        self.standings_reader = standings_reader

    def getRelevantStandings(self):
        teams_list = []
        for team_name in self.standings_reader.team_winning_pcts.keys():
            new_team = TeamInfo(team_name)
            new_team.populateTeamData(self.standings_reader.team_winning_pcts, self.standings_reader.team_conferences, self.standings_reader.division_leaders, self.picks.contestant_picks)
            teams_list.append(new_team)
        #sort the afc results first by adding 10 to their max 1.00 winning pct, then sort by winning pct
        teams_list.sort(key=lambda team_entry: 10.0 + team_entry.winning_pct if team_entry.conference == AFC else team_entry.winning_pct, reverse=True)
        notifier.notify(teams_list)


if __name__ == "__main__":
    picks_reader = PicksStub()
    notifier = SpyNotifier()
    standings_reader =  NflWebReader()
    teamStatus = standings_reader.setTeamData()
    standingsStatus = standings_reader.populateStandings()
    send_standings = SendWeeklyStandings(picks_reader, notifier, standings_reader)  
    standingStatus = send_standings.getRelevantStandings()
    allStatuses = teamStatus + standingsStatus 
    if len(allStatuses) != 0:
        notifier.alert("\n".join(allStatuses))

