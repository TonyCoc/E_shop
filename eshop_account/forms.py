from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core import validators



class user_edit_f(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام'}),
        validators=[validators.MaxLengthValidator(15, message='طول زیاد')]
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی'}))





class login(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری', 'name': 'userName'}),
        label='',

    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور', 'name': 'passWord'}),
        label=''
    )


user = get_user_model()


class register(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری', 'name': 'userName'}),
        validators=[validators.MinLengthValidator(4,message="نام کاربری حداقل باید 4 کاراکتر باشد")],
        label=''
    )

    def clean_user_name(self):

        user_name = self.cleaned_data.get('user_name')
        qs = user.objects.filter(username=user_name)
        if qs.exists():
            raise forms.ValidationError('نام کاربری یا ایمیل قبلا استفاده شده')
        return user_name

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'ایمیل'}),
        label='', )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_name = self.cleaned_data.get('user_name')
        qs = user.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('نام کاربری یا ایمیل قبلا استفاده شده')
        return email

    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام'}))

    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی'}))

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}),
        label=''
    )
    password_2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'تایید رمز عبور'}),
        label=''
    )

    def clean_password_2(self):
        pass1 = self.cleaned_data.get('password')
        if len(pass1) < 8:
            raise forms.ValidationError('رمز عبور حداقل باید 8 کاراکتر باشد')
        pass2 = self.cleaned_data.get('password_2')
        if pass1 != pass2:
            raise forms.ValidationError('لطفا رمز عبور خود را درست تایید کنید')
        return pass2
