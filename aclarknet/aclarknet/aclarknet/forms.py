from django import forms


class ContactForm(forms.Form):
    email = forms.CharField(label='Your email address (required):', widget=forms.TextInput(attrs={'class' : 'email'}))
    message = forms.CharField(label='How can we help (required):', widget=forms.Textarea(attrs={'class' : 'message'}))
    message2 = forms.CharField(label='How did you hear about us (optional):', required=False, widget=forms.Textarea(attrs={'class' : 'message2'}))
