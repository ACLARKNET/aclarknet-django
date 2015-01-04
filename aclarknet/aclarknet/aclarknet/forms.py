from django import forms


class ContactForm(forms.Form):
    email = forms.CharField(label='Email')
    message = forms.CharField(label='Message')
