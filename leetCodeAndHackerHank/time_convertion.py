# https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true

def timeConversion(s):
    hours = s[0:2]
    minutes = s[3:5]
    seconds = s[6:8]
    moment = s[8:11]
    if moment == 'AM':
      hours = int(hours)%12
    else:
      hours = (int(hours)%12) + 12
    return f"{hours}".rjust(2, "0") + ":{}:{}".format(minutes, seconds)
