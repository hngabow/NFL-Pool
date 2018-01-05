class SpyNotifier():
    def alert(self, error_message):
        print error_message
    def notify(self, team_infos):
        for info in team_infos:
            if len(info.contestants) > 0:
                print info.team_name, info.winning_pct

