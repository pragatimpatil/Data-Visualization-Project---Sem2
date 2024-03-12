# forms.py

from django import forms

class QnAForm(forms.Form):
    user_question = forms.CharField(label='Your Question', widget=forms.TextInput(attrs={'class': 'form-control'}))
