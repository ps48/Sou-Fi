from django import forms
from .models import Message

class SendMessage(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('msg',)
