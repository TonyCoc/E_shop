from django import forms
from django.core import validators


class Contact_us_form(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "نام و نام خانوادگی", "class": "form-control"}),
        validators=[
            validators.MaxLengthValidator(50, 'نام و نام خانوادگی وارد شده نباید بیشتر از 50 کاراکتر باشند')
        ]

    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "ایمیل", "class": "form-control"}),
        validators=[
            validators.MaxLengthValidator(150, 'ایمیل وارد شده نباید بیشتر از 150 کاراکتر باشند')
        ]

    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "عنوان", "class": "form-control"}),
        validators=[
            validators.MaxLengthValidator(70, 'موضوع وارد شده نباید بیشتر از 70 کاراکتر باشند')
        ]

    )
    text = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "پیام شما", "class": "form-control"}),

    )
