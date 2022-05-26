from django.shortcuts import render
from .forms import Contact_us_form
from .models import Contact_us_model
from eshop_settings.models import Settings


def contact_us_view(request):
    contact_form = Contact_us_form(request.POST or None)
    setting = Settings.objects.first()
    if contact_form.is_valid():
        full_name = contact_form.cleaned_data.get('full_name')
        email = contact_form.cleaned_data.get('email')
        subject = contact_form.cleaned_data.get('subject')
        text = contact_form.cleaned_data.get('text')
        Contact_us_model.objects.create(full_name=full_name, email=email, subject=subject, text=text)
        contact_form = Contact_us_form()

    context = {
        "Form": contact_form,
        "setting": setting
    }

    return render(request, 'contact_us.html', context)
