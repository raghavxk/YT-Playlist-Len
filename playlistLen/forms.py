from django import forms


class URLform(forms.Form):
    url_of_playlist = forms.CharField(label=False)
