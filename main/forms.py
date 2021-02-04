from django import forms

choices = [('Basic Website', 'Basic Website'), ('Standard Website', 'Standard Website'), ('Business Website', 'Business Website')]

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    package = forms.CharField(label="Which website are you interested in?", widget=forms.Select(choices=choices))
    message = forms.CharField(max_length=1000, widget=forms.Textarea)


