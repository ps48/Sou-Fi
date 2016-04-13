from DTMFdetector import DTMFdetector
dtmf = DTMFdetector()
data = dtmf.getDTMFfromWAV("ns2.wav")
print data