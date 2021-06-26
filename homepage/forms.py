from django import forms
from django.core.validators import FileExtensionValidator

class ContactForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name'}),label='Name',max_length=50,required=True)
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email'}),label='Email',max_length=50,required=True)
    subject=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Subject'}),label='Subject',max_length=50)
    message=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Message'}),label='Message',max_length=200)