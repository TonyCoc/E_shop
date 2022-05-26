from django import forms


class order_form(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput)
    count = forms.IntegerField(widget=forms.NumberInput)
