#!/usr/bin/python
# code to email a message stored in file 'message'
# can set subject, recipients, blind cc recipient

import subprocess

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

halEC,halEP,aaronE,contestantsE= read_addresses()

# some calls and relevant files
mailer("'NFL Pool: Worst Season Ever'", 'HalEC', contestantsE, 'nfl')
#mailer("'NFL Pool: Worst Season Ever'", '', halEC, 'nfl')
#mailer("'need picks'", halEC, aaronE, 'football_need')
#mailer("'need picks'", '', halEP, 'nfl')

#football_addresses is a file containing contestant emails
#football_need is a file containing request for picks, sent in August
#nfl is a file containing the new standings message'
