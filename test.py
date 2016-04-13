import os

cmd = "sox s.wav -C 256 -r 16000 ns2.wav"

print os.system(cmd)