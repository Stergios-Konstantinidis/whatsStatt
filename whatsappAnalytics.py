import re
import datetime
from message import message

def GetCount(file):
    allMessagesExploitables = []
    file = open(file, 'r')
    for x in file:
        try:
            reg = re.match("\[(.*)\] ([^:]+):(.+)",x)
            date = datetime.datetime.strptime(reg[1],"%d.%m.%Y, %H:%M:%S")
            user = reg[2]
            chars = len(reg[3])
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


