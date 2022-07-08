import time

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout, get_user_model
from eshop_user_profile.models import Profile_photo
import random
from .forms import *
from django.contrib.auth.models import User
from django.core.mail import send_mail


# from .models import Reset_code


def login_form(request):
    Login_ref = login(request.POST or None)
    context = {
        'Login_form': Login_ref,
        'error': False
    }
    if Login_ref.is_valid():

        if not Login_ref.cleaned_data.get("remember_me"):
            request.session.set_expiry(0)
        userName = Login_ref.cleaned_data.get('user_name')
        passWord = Login_ref.cleaned_data.get('password')
        user = authenticate(request, username=userName, password=passWord)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            context['error'] = True

    return render(request, 'auth/login.html', context)


def log_out(request):
    logout(request)
    return redirect('/')


User = get_user_model()


def register_form(request):
    register_ref = register(request.POST or None)
    context = {
        'form': register_ref
    }
    if register_ref.is_valid():
        userName = register_ref.cleaned_data.get('user_name')
        email = register_ref.cleaned_data.get('email')
        password = register_ref.cleaned_data.get('password')
        first_name = register_ref.cleaned_data.get('first_name')
        last_name = register_ref.cleaned_data.get('last_name')
        User.objects.create_user(username=userName, email=email, password=password, first_name=first_name,
                                 last_name=last_name)
        user = authenticate(request, username=userName, password=password)
        auth_login(request, user)
        Profile_photo.objects.create(user_id=request.user.id)
        return redirect('/')
    return render(request, 'auth/register.html', context)


@login_required(login_url='/login')
def user_panel(request):
    context = {}
    return render(request, 'user_panel.html', context)


@login_required(login_url='/login')
def user_edit(request):
    user_cur = User.objects.get(id=request.user.id)
    form_edit = user_edit_f(request.POST or None,
                            initial={'first_name': user_cur.first_name, 'last_name': user_cur.last_name})
    context = {
        'form': form_edit
    }
    if request.method == 'POST':
        try:
            image = request.FILES['image']
            user_cur.profile_photo.photo = image
            user_cur.profile_photo.save()
        except:
            pass
    if form_edit.is_valid():
        first_name = form_edit.cleaned_data.get('first_name')
        last_name = form_edit.cleaned_data.get('last_name')
        user_cur.first_name = first_name
        user_cur.last_name = last_name
        if request.POST.get('email') == user_cur.email:
            context['user_name_len'] = True
            pass
        if len(request.POST.get('user_name')) < 4:
            return render(request, 'edit_panel.html', context)
        email_qs = User.objects.filter(email=request.POST.get('email'))
        user_name_qs = User.objects.filter(username=request.POST.get('user_name'))
        if request.POST.get('email') != user_cur.email and not email_qs.exists():
            user_cur.email = request.POST.get('email')

        if request.POST.get('user_name') == request.user.get_username():
            pass
        if request.POST.get('user_name') != user_cur.get_username() and not user_name_qs.exists():
            user_cur.username = request.POST.get('user_name')
        if user_name_qs.exists() and request.POST.get('user_name') != user_cur.get_username():
            if email_qs.exists() and request.POST.get('email') != user_cur.email:
                context['user_name_error'] = True
                context['email_error'] = True
                return render(request, 'edit_panel.html', context)
            context['user_name_error'] = True
            return render(request, 'edit_panel.html', context)
        if email_qs.exists() and request.POST.get('email') != user_cur.email:
            if user_name_qs.exists() and request.POST.get('user_name') != user_cur.get_username():
                context['user_name_error'] = True
                context['email_error'] = True
                return render(request, 'edit_panel.html', context)
            context['email_error'] = True
            return render(request, 'edit_panel.html', context)
        user_cur.save()
        return redirect('/user-panel')
    return render(request, 'edit_panel.html', context)


def reset_password(request):
    reset_password_ref = reset_password_form(request.POST or None)
    context = {
        "form": reset_password_ref,
        'tryed_times': None,
        "tryed_error" : None
    }
    if reset_password_ref.is_valid():
        email = reset_password_ref.cleaned_data.get("email")

        reset_code = reset_password_ref.cleaned_data.get("reset_code")

        user_cur = User.objects.filter(email=email).first()
        if user_cur.reset_password.is_unvalidated:
            context['tryed_error'] = True
        else:
            context['tryed_times'] = user_cur.reset_password.reset_try_count
            password = reset_password_ref.cleaned_data.get("password")

            user_real_reset_code = user_cur.reset_password.reset_code

            if reset_code == user_real_reset_code :
                user_cur.set_password(password)
            user_cur.reset_password.reset_try_count += 1
            user_cur.reset_password.save()
            user_cur.save()
            time.sleep(1.5)
            return redirect('/login')
    return render(request,'auth/resetPass.html',context=context)