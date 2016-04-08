import datetime

def rev(s):
    return s[::-1]

def idToHash(n):
    smap = "ABCD*#0123456789"
    ###(E: * , F: #)
    shorturl = ""
    while(n!=0):
        a = int(n%256)
        a = int(a%16)
        shorturl = shorturl + smap[a]
        n = int(n/256)
    shorturl = rev(shorturl)
    return shorturl

##def getHash(nowt):
##    i = 0
##    x = ""
##    while len(x)<14:
##        if(nowt[i]>="0" and nowt[i]<="9"):
##            x=x+nowt[i];
##        i=i+1
##    n = int(x)
##    url = idToHash(n)
##    return url

