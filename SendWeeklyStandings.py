from PicksReaders import PicksFileReader, PicksStub
from ContestantsNotifier import SpyNotifier 
from StandingsReaders import NflWebReader

class SendWeeklyStandings(object):
    def __init__(self, picks_reader, notifier, standings_reader):
        self.picks = picks_reader
        self.notifier = notifier
        self.standings_reader = standings_reader

    def getRelevantStandings(self):
        error_list = []
        afc_results = []
        nfc_results = []
        for contestant, picks in self.picks.contestant_picks.iteritems():
            for pick in picks:
                if pick not in self.standings_reader.nfc_standings and pick not in self.standings_reader.afc_standings:
                    error_list.append(pick + " not in NFL standings")
            afc_results.append((contestant, picks[0], self.standings_reader.afc_standings[picks[0]]))
            nfc_results.append((contestant, picks[1], self.standings_reader.nfc_standings[picks[1]]))
        afc_results.sort( key=lambda team_entry: team_entry[2], reverse=True)
        nfc_results.sort( key=lambda team_entry: team_entry[2], reverse=True)
        if len(error_list) != 0:
            notifier.alert(error_list)
        else:
            notifier.notify(afc_results, nfc_results)


if __name__ == "__main__":
    picks_reader = PicksStub()
    notifier = SpyNotifier()
    standings_reader =  NflWebReader()
    standings_reader.setTeamData()
    standings_reader.populateStandings()
    send_standings = SendWeeklyStandings(picks_reader, notifier, standings_reader)  
    send_standings.getRelevantStandings()
