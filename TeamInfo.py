
class TeamInfo(object):
    def __init__(self, name):
        self.team_name = name
        self.winning_pct = 0.0
        self.contestants = []
        self.leading_division = ""

    def populateTeamData(self, winning_pcts, conference_membership, division_info, contestant_picks):
        self.winning_pct = winning_pcts[self.team_name]
        self.conference = conference_membership[self.team_name]
        for division, leaders in division_info.iteritems():
            for leader in leaders:
                if leader == self.team_name:
                    self.leading_division =  division
        for contestant, picks in contestant_picks.iteritems():
            for pick in picks:
                if pick == self.team_name:
                    self.contestants.append(contestant)



