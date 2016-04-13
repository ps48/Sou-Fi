import wave
import os 

def make_audio_file(text):
	tones=dict()
	tones["0"]="waves/0.wav"
	tones["1"]="waves/1.wav"
	tones["2"]="waves/2.wav"
	tones["3"]="waves/3.wav"
	tones["4"]="waves/4.wav"
	tones["5"]="waves/5.wav"
	tones["6"]="waves/6.wav"
	tones["7"]="waves/7.wav"
	tones["8"]="waves/8.wav"
	tones["9"]="waves/9.wav"
	tones["A"]="waves/A.wav"
	tones["B"]="waves/B.wav"
	tones["C"]="waves/C.wav"
	tones["D"]="waves/D.wav"
	tones["#"]="waves/P.wav"
	tones["*"]="waves/S.wav"

	infiles = []
	for ch in text:
		infiles.append(tones[ch])

	outfile = "sounds.wav"

	data= []
	for infile in infiles:
	    w = wave.open(infile, 'rb')
	    data.append( [w.getparams(), w.readframes(w.getnframes())] )
	    w.close()

	output = wave.open(os.getcwd()+"/static/"+outfile, 'wb')
	output.setparams(data[0][0])
	for i in range(len(infiles)):
		output.writeframes(data[i][1])
	output.close()


	

