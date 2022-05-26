from django import forms


class image_input(forms.Form):
    image = forms.ImageField(widget=forms.FileInput())
