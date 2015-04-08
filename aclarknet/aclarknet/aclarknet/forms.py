from django import forms


class ContactForm(forms.Form):
    email = forms.CharField(label='Your email address:', widget=forms.TextInput(attrs={'class' : 'email'}))
    message = forms.CharField(label='How can we help:', widget=forms.Textarea(attrs={'class' : 'message'}))
    message2 = forms.CharField(label='How did you hear about us:', widget=forms.Textarea(attrs={'class' : 'message2'}, required=False))
