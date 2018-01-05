#!/usr/bin/python
# code to email a message stored in file 'message'
# can set subject, recipients, blind cc recipient

import subprocess
from TeamInfo import TeamInfo
from NflSiteStrings import * 

def mailer(subject, blind_copy, mail_to, message):
#subject, blind_copy, and mail_to must be strings without whitespace
#message is a string, the name of a text file containing the mail message

   mail_command = '/usr/bin/Mail -s' + subject
   if blind_copy != '':
      mail_command += ' -b' + blind_copy
   mail_command += ' ' + mail_to + " < " + message
   p= subprocess.Popen(mail_command ,shell= True)

def read_addresses():
   with open("football_addresses", "r") as emails:
      numLines = int( emails.readline().strip("\n") )
      a=[emails.readline().strip("\n") for i in range(0,numLines)]
      return a

#halEC,halEP,aaronE,contestantsE= read_addresses()

# some calls and relevant files
#mailer("'need picks'", hal, aaron, 'football_need')
#mailer("'need picks'", '', halEP, 'nfl')
#mailer("'need picks'", '', "`cat football_addresses_2`", 'nfl')

#football_addresses is a file containing contestant emails
#football_need is a file containing request for picks, sent in August
#nfl is a file containing the new standings message'

def formatStandingsMail(sorted_team_list, week):
    afc_summary = ""
    nfc_summary = ""
    #should be approximately as many afc teams as nfc teams
    nfc_start = len(sorted_team_list) >> 1
    while sorted_team_list[nfc_start].conference == AFC and nfc_start < len(sorted_team_list):
        nfc_start += 1
    while sorted_team_list[nfc_start - 1].conference == NFC and nfc_start > 0:
        nfc_start -= 1
    afc_leader = sorted_team_list[0].winning_pct 
    nfc_leader = sorted_team_list[nfc_start].winning_pct
    for team_index in range(0, nfc_start):
        team_info = sorted_team_list[team_index]
        if len(team_info.contestants) > 0 or (team_info.winning_pct == afc_leader and afc_leader < 1.00):
            afc_summary += team_info.team_name + "\t" + str(team_info.winning_pct) + "\t" + \
                           team_info.leading_division + "\t" + ",".join(team_info.contestants) + "\n"
        if team_index + 1 != nfc_start and sorted_team_list[team_index + 1].winning_pct != afc_leader and sorted_team_list[team_index].winning_pct == afc_leader:
            afc_summary += "------------------------------------------------------------------------------------------\n"

    for team_index in range(nfc_start, len(sorted_team_list)):
        team_info = sorted_team_list[team_index]
        if len(team_info.contestants) > 0 or (team_info.winning_pct == nfc_leader and nfc_leader < 1.00):
            nfc_summary += team_info.team_name + "\t" + str(team_info.winning_pct) + "\t" + \
                           team_info.leading_division + "\t" + ",".join(team_info.contestants) + "\n"
        if team_index + 1 != len(sorted_team_list) and sorted_team_list[team_index + 1].winning_pct != nfc_leader and sorted_team_list[team_index].winning_pct == nfc_leader :
            nfc_summary += "------------------------------------------------------------------------------------------\n"
    template = """Standings after week %i of 17
D=division leader, T=tied for division leader
    ********AFC********
Team\t\tPct\tDivLeader\tPickedBy
Best In AFC
%s
    ********NFC********
Team\t\tPct\tDivLeader\tPickedBy
Best In NFC
%s
""" % (week, afc_summary, nfc_summary)
    return template
