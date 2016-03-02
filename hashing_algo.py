import datetime

def rev(s):
    return s[::-1]

def idToHash(n):
    smap = "ABCDEF0123456789"
    ###(E: * , F: #)
    shorturl = ""
    while(n!=0):
        a = int(n%128)
        a = int(a%16)
        shorturl = shorturl + smap[a]
        n = int(n/128)
    shorturl = rev(shorturl)
    return shorturl

def hashToId(surl):
    ts = 0
    for i in surl:
        if("A"<=i and i<="F"):
            ts = ts*128 + ord(i) - ord('A')
        if("0"<=i and i<="9"):
            ts = ts*128 + ord(i) - ord('0') + 6;
    return ts

nowt = str(datetime.datetime.now())
print(nowt)
i = 2
x = ""
while len(x)<12:
    if(nowt[i]>="0" and nowt[i]<="9"):
        x=x+nowt[i];
    i=i+1
print("TimeStamp : ",x)
n = int(x)
url = idToHash(n)
print("ShortURL : ",url)
#ts = hashToId(url)
#print(ts)

