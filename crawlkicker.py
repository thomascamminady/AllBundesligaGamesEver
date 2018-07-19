import os

for k in range(63,100):
    print(k)
    url = 'http://www.kicker.de/news/fussball/bundesliga/spieltag/1-bundesliga/19'
    url += str(k)
    url += '-'
    if k<99:
        url += str(k+1)
    else:
        url += '00'
    url += '/-1/0/spieltag.html'
    command = 'wget ' + url
    print(command)
    os.system(command)

for k in range(0,18):
    print(k)
    url = 'http://www.kicker.de/news/fussball/bundesliga/spieltag/1-bundesliga/20'
    if k<10:
        url += '0'
        url += str(k)
    else:
        url += str(k)

    url += '-'
    if k+1<10:
        url += '0'
        url += str(k+1)
    else:
        url += str(k+1)

    url += '/-1/0/spieltag.html'
    command = 'wget ' + url
    print(command)
    os.system(command)

