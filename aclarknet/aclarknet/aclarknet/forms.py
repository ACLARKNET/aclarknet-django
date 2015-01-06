from django import forms


class ContactForm(forms.Form):
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class' : 'email'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class' : 'message'}))
