from django.shortcuts import render,redirect
from .forms import SendMessage
from .models import Message
import hashing_algo
import datetime
import wavegen

# Create your views here.

def homepg(request):
    msgs = Message.objects.all()
    return render(request,'soufi/homepg.html',{'msgs':msgs})

def send_msg(request):
    if request.method == "POST":
        form = SendMessage(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.ts = datetime.datetime.now()
            nowt = str(post.ts)
            i = 0
            ts = ""
            while len(ts)<14:
                if(nowt[i]>="0" and nowt[i]<="9"):
                    ts=ts+nowt[i];
                i=i+1
            n = int(ts)
            post.hashkey = hashing_algo.idToHash(n)
            hk = post.hashkey
            wavegen.make_audio_file(hk)
            post.save()
            return redirect('play_audio')
    else:
        form = SendMessage()
    return render(request,'soufi/send_msg.html',{'form':form})

def play_audio(request):
    return render(request,'soufi/play_audio.html')


