from Mailer import *
from TeamInfo import TeamInfo
from NflSiteStrings import AFC, NFC
import pytest

class TestMailer(object):
    def getTemplate(self):
        return """Standings after week %i of 17
D=division leader, T=tied for division leader
    ********AFC********
Team\t\tPct\tDivLeader\tPickedBy
Best In AFC
%s
    ********NFC********
Team\t\tPct\tDivLeader\tPickedBy
Best In NFC
%s
""" 
    def test_formatStandingsMail_when_all_teams_at_1(self):
        expected = self.getTemplate() % (1, "Denver Broncos\t1.0\t\tAaron,Bill\n", "Green Bay Packers\t1.0\t\tAaron,Bill\n")
        teams = [TeamInfo("Denver Broncos", 1.00, ["Aaron", "Bill"], AFC, ""),
                  TeamInfo("New England Patriots", 1.00, [], AFC, ""),
                  TeamInfo("Atlanta Falcons", 1.00, [], NFC, ""),
                  TeamInfo("Green Bay Packers", 1.00, ["Aaron", "Bill"], NFC, "")]
        output = formatStandingsMail(teams, 1)
        assert output == expected
    
    def test_formatStandingsMail_when_many_afc_teams(self):
        expected = self.getTemplate() % (1, """Denver Broncos\t1.0\t\tAaron,Bill
------------------------------------------------------------------------------------------
New England Patriots\t0.2\t\tSasha\n""",
                   "Green Bay Packers\t1.0\t\tAaron,Bill,Sasha\n" )
        teams = [TeamInfo("Denver Broncos", 1.00, ["Aaron", "Bill"], AFC, ""),
                 TeamInfo("Miami Dolphins", .99, [], AFC, ""),
                 TeamInfo("Pittsburgh Steelers", .60, [], AFC, ""),
                 TeamInfo("New England Patriots", .20, ["Sasha"], AFC, ""),
                 TeamInfo("Green Bay Packers", 1.00, ["Aaron", "Bill", "Sasha"], NFC, "")]
        output = formatStandingsMail(teams, 1)
        assert output == expected

    def test_formatStandingMail_when_many_ncf_teams(self):
        expected = self.getTemplate() % (1, """Denver Broncos\t1.0\t\tAaron,Bill
------------------------------------------------------------------------------------------
New England Patriots\t0.2\t\tSasha\n""",
"""Green Bay Packers\t1.0\t\tAaron
Baltimore Ravens\t1.0\t\tSasha
------------------------------------------------------------------------------------------
Houston Texans\t0.3\t\tBill\n""")
        teams = [TeamInfo("Denver Broncos", 1.00, ["Aaron", "Bill"], AFC, ""),
                TeamInfo("New England Patriots", .20, ["Sasha"], AFC, ""),
                TeamInfo("Green Bay Packers", 1.00, ["Aaron"], NFC, ""),
                TeamInfo("Buffalo Bills", 1.00, [], NFC, ""),
                TeamInfo("Baltimore Ravens", 1.00, ["Sasha"], NFC, ""),
                TeamInfo("Houston Texans", .30, ["Bill"], NFC, ""),
                TeamInfo("Oakland Raiders", .10, [], NFC, "")]
        output = formatStandingsMail(teams, 1)
        print output
        print expected
        assert output == expected
