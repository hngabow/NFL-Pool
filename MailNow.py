#!/usr/bin/python
# our code is executed by Cron at 4AM on Monday and Tuesday of each week
# check_done() exits the run if it's Monday and a picked team will play in MNF
# the file ToDoFile is set on Monday to contain either
# "Done" if the week's standings have been mailed, so no mail will be sent Tuesday
# "Not Done" if the standings should be mailed Tuesday
# 

import datetime
# print "Day of week: ", datetime.date.today().strftime("%a")
# Day of week:  Tue
# %A gives full name, eg Tuesday
# %a gives abbreviated name, eg Tue
from StandingsReaders import NflWebReader
#aaron: i only need hasPlayed
# should this be import StandingsReaders
import PicksReaders

def check_done():
   this_day = datetime.date.today().strftime("%a")
   if this_day == 'Mon':
      for team in PicksReaders.contestant_picks.values() 
          if not NflWebReader.hasPlayed(team):
              with open ('ToDoFile',"w") as todo:
                 todo.write("Not done")
                 exit()
      with open ('ToDoFile',"w") as todo:
                 todo.write("Done")
      #continue to eventually send out the standings
   else: #this_day == 'Tue'
      with open ('ToDoFile',"r") as todo:
           status = todo.readline().strip("\n")
           if status == "Done":
               exit()
      #continue to eventually send out the standings

