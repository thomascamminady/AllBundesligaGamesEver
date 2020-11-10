import string
import re



def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def main():
    # my code here
    filename ="Spieltag/spieltag.html"
    for season in range(55):
        if season>0:
            y = filename +"."+ str(season)
        else:
            y = filename

        with open(y) as f:
            lines = f.readlines()
            lastspieltag ="dummy"
            timeflag = False
            nextyearflag = False
            for line in lines:        
                if timeflag:
                    date = find_between(line,"<td>","&") # find date of game
                    time = find_between(line,";","<")    # find time of game
                    lastdate = date;    # save this 
                    lasttime = time;
                    timeflag = False
                if "class=\"first\">" in line:
                    if "&nbsp" not in line:
                        day = find_between(line,"rst\">","<")
                        lastday = day;
                        timeflag = True
                home = find_between(line,"ovVrn ovVrnRight\">", "</a>"); # home team name
                if len(home)>0:
                    x = lastspieltag.split(".")
                    x = x[0]
                    if season+63<100:
                        print("19"+str(season+63)),
                    elif season+63<110:
                        print("200"+str(season+63-100)),
                    else:
                        print("20"+str(season+63-100)),
                    print(" , "),
                    if season+1+63<100:
                        print("19"+str(season+1+63)),
                    elif season+1+63<110:
                        print("200"+str(season+1+63-100)),
                    else:
                        print("20"+str(season+1+63-100)),

                    print(" , "),
                    print(x), 
                    print(" , "),
                    if lastday=="Sa":
                        print("Saturday"),
                    if lastday=="So":
                        print("Sunday"),
                    if lastday=="Mo":
                        print("Monday"),
                    if lastday=="Di":
                        print("Tuesday"),
                    if lastday=="Mi":
                        print("Wednesday"),
                    if lastday=="Do":
                        print("Thursday"),
                    if lastday=="Fr":
                        print("Friday"),



                    #print(lastday),
                    print(" , "),
                    month = lastdate[3:5]
                    month = int(month)
                    if month<4:
                        nextyearflag = True
                    lastdate = string.replace(lastdate,".","/")
                    if nextyearflag:
                        if season+1+63<100:
                            d = (lastdate+"19"+str(season+1+63)),
                        elif season+1+63<110:
                            d = (lastdate+"200"+str(season+1+63-100)),
                        else:
                            d = (lastdate+"20"+str(season+1+63-100)),

                    else:
                        if season+63<100:
                            d = (lastdate+"19"+str(season+63)),
                        elif season+63<110:
                            d = (lastdate+"200"+str(season+63-100)),
                        else:
                            d = (lastdate+"20"+str(season+63-100)),
                    d = string.split(d[0],"/")
                    out = d[2]+"-"+d[1]+"-"+d[0]
                    out = string.replace(out," ","")
                    print(out),

                    print(" , "),
                    print(lasttime),
                    print(" , "),
                    print(home), 
                    print(" , "),
                guest = find_between(line,"class=\"ovVrn\">","</a>")
                if len(guest)>0:
                    print(guest), 
                    print (" , "),
                score = find_between(line,"<td class=\"alignleft nowrap\" >","</td>")
                if len(score)>0:
                    score = string.replace(score,'&nbsp;(',' , ')
                    score = string.replace(score,')', ' ')
                    tmp = string.split(score,',')
                    if len(tmp)==1: # if half time score is missing add it as 0:0
                        score += ", 0:0"
                    print(score),
                    print(','),
                    s = string.split(score,',')
                    x = string.split(s[0],':');
                    print(x[0]),
                    print(','),
                    print(x[1]),
                    print(','),
                    x = string.split(s[1],':');
                    print(x[0]),
                    print(','),
                    print(x[1]),
                    print(","),
                    # get points
                    x = string.split(s[0],':');
                    if x[0]=="-":
                        print(0),
                        print(","),
                        print(0)
                    elif len(x[0])>0:
                        if int(x[0])>int(x[1]):
                            if season+63<95: # the 3 point rule came into place in 1995, before that a win was 2 points
                                print(2),
                            else:
                                print(3),
                            print(","),
                            print(0)

                        elif int(x[1])>int(x[0]):
                            print(0),
                            print(","),
                            if season+63<95:
                                print(2)
                            else:
                                print(3)

                        else:
                            print(1),
                            print(","),
                            print(1)



                spieltag = find_between(line,"","<span id=\"ovSpieltagTippspielStatus")
                if len(spieltag)>0:
                    lastspieltag = spieltag








if __name__ == "__main__":
    main()
