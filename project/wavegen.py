import wave

def make_audio_file(text):
	tones=dict()
	tones["0"]="0.wav"
	tones["1"]="1.wav"
	tones["2"]="2.wav"
	tones["3"]="3.wav"
	tones["4"]="4.wav"
	tones["5"]="5.wav"
	tones["6"]="6.wav"
	tones["7"]="7.wav"
	tones["8"]="8.wav"
	tones["A"]="A.wav"
	tones["B"]="B.wav"
	tones["C"]="C.wav"
	tones["D"]="D.wav"
	tones["#"]="P.wav"
	tones["*"]="S.wav"

	infiles = []
	for ch in text:
		infiles.append(tones[ch])

	outfile = "C:\\Python33\\virtualenv-15.0.0\\python3-workspace\\project\\soufi\\static\\soufi\\sounds.wav"

	data= []
	for infile in infiles:
	    w = wave.open(infile, 'rb')
	    data.append( [w.getparams(), w.readframes(w.getnframes())] )
	    w.close()

	output = wave.open(outfile, 'wb')
	output.setparams(data[0][0])
	for i in range(len(infiles)):
		output.writeframes(data[i][1])
	output.close()
