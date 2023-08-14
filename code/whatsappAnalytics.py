import re
import datetime
import numpy
from message import message
from PyQt5.QtCore import QDate


def GetCount(file, _qDate:QDate = QDate(1900,1,1)):
    allMessagesExploitables = []
    file = open(file, 'r')
    for x in file:
        try:
            reg = re.match("\[(.*)\] ([^:]+):(.+)",x)
            date = datetime.datetime.strptime(reg[1],"%d.%m.%Y, %H:%M:%S")
            user = reg[2]
            chars = len(reg[3])
            if date.date() > _qDate.toPyDate():
                msg = message(date, user, chars)
                allMessagesExploitables.append(msg)
        except:
            pass
    userStats = {}
    for envoi in allMessagesExploitables:
        try:
            userStats[envoi.getUser()] = userStats[envoi.getUser()] +1
        except:
            userStats[envoi.getUser()] = 1

    res = sorted(userStats.items(), key=lambda x:x[1])
    to_return = []
    for user in res:
        to_return.append(str(user[0]) + " à envoyé "+ str(user[1]) + " messages")
    return to_return




def getDailyCount(files,_qDate:QDate = QDate(1900,1,1)):
    allMessagesExploitables = []
    file = open(files, 'r')
    for x in file:
        try:
            reg = re.match("\[(.*)\] ([^:]+):(.+)",x)
            date = datetime.datetime.strptime(reg[1],"%d.%m.%Y, %H:%M:%S")
            user = reg[2]
            chars = len(reg[3])
            if date.date() > _qDate.toPyDate():
                msg = message(date, user, chars)
                allMessagesExploitables.append(msg)
        except:
            pass


    names = tuple()

    dates = []
    for envoi in allMessagesExploitables:
        if not str(envoi.getDate()) in names:
            dates.append(envoi.getDate())


    DailyStats = {}
    for envoi in allMessagesExploitables:
        if envoi.getUser() not in DailyStats:
            names = names + tuple(envoi.getUser())
            DailyStats[envoi.getUser()] = list(map(lambda x: 0, dates))
        DailyStats[envoi.getUser()][dates.index(envoi.getDate())] = DailyStats[envoi.getUser()][dates.index(envoi.getDate())] + 1

    for stat in DailyStats:
        DailyStats[stat] = numpy.array(DailyStats[stat])

    return names, dates, DailyStats