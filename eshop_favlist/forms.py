from django import forms

class Fave_list_form(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput)