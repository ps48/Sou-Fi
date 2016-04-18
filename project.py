from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Msgkey
from DTMFdetector import DTMFdetector
from nocache import nocache
import os
import hashing_algo
import datetime
import wavegen
import base64

app = Flask(__name__)
engine = create_engine('sqlite:///soufi.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/home')
def index():
	return render_template('home.html')

@app.route('/sender/msg')
def send_msg():
	return render_template('send_msg.html')

@app.route('/receive/msg')
def rec_msg():
	return render_template('rec_msg.html')

@app.route('/sender/play', methods=['GET', 'POST'])
@no_cache
def send_play():
	if request.method == 'POST':
		ts = datetime.datetime.now()
		nowt = str(ts)
		i = 0
		ts = ""
		while len(ts)<14:
		    if(nowt[i]>="0" and nowt[i]<="9"):
		        ts=ts+nowt[i];
		    i=i+1
		n = int(ts)
		hashkey = hashing_algo.idToHash(n)
		wavegen.make_audio_file(hashkey)

		newmsg = Msgkey(hash_key=hashkey,name=str(request.form['msg']))
		session.add(newmsg)
		session.commit()
		return render_template('send_play.html',msg = request.form['msg'],hashkey=hashkey)

@app.route('/receive/hash', methods=['GET', 'POST'])
def rec_hash():
	if request.method == 'POST':
		base= request.form['sound']
		base=base.replace("data:audio/wav;base64,","")
		wavefile = base64.b64decode(base)
		filename = 's.wav'  # I assume you have a way of picking unique filenames
		with open(filename, 'wb') as f:
			f.write(wavefile)
		cmd = "sox s.wav -C 256 -r 16000 ns2.wav"
		print os.system(cmd)
		dtmf = DTMFdetector()
		data = dtmf.getDTMFfromWAV("ns2.wav")

		new_str="%"
		for i in range(len(data)):
			new_str=new_str+data[i]+"%"

		try:
			msg_val = session.query(Msgkey).filter(Msgkey.hash_key.like(new_str)).one()
			# return render_template('rec_hash.html',msg = base)
			return msg_val.name
		except:
			return data


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
