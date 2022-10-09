import re

TIME_LENGTH = 29
HOURS1 = 2
MIN1 = 5
SEC1 = 8
MS1 = 12
ENDSTAMP = 17
HOURS2 = 19
MIN2 = 22
SEC2 = 25
MS2 = 29

def isCount(line):
    digit = line.replace('\n', '')
    return digit.isdigit()

def isTime(line):
    timeStamp = re.compile('^[0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3} --> [0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3}')
    return timeStamp.match(line)

