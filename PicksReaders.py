class PicksFileReader(object):
    def __init__(self):
        self.contestant_picks = {}
        with open("Picks.txt", "r") as picks_file:
            for line in picks_file:
                pick_info = line.strip().split("\t")
                self.contestant_picks[pick_info[0]] = pick_info[1]

class PicksStub(object):
    def __init__(self):
       self.contestant_picks = {'Aaron':('Denver Broncos', 'New York Giants'), 'Hal':('Baltimore Ravens', 'Atlanta Falcons')}

