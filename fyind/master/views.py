from django.contrib import messages
from django.core.mail import EmailMessage
from django.forms import ModelForm
from django.shortcuts import render, redirect
from crispy_forms.helper import FormHelper
from django.template.loader import render_to_string

from .models import *


class Form(ModelForm):
    class Meta:
        model = Application
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False


def index(request):
    form = Form(request.POST or None)
    if request.method == 'POST':
        print(form.errors)
        if form.is_valid():
            application = form.save(commit=False)
            application.status = "IP"
            application.save()
            subject = 'Thank you for your time, ' + application.company
            message = render_to_string('emailTemplate.html', {
                'name': application.contact_name,
                'company': application.company_name,
                'email': application.email,
                'phone':application.phone_number
            })
            email = EmailMessage(subject, message, from_email='service@fyind.io', to=[application.email],
                                 bcc=['nitin@kamadhenu.io'])
            email.send()
            messages.success(request, 'Thank you for taking out time and filling out the form. A confirmation mail '
                                      'has been sent to you. We will be reaching out to you soon to carry this '
                                      'forward.')
            return redirect('index')
        else:
            form = Form()
    return render(request, 'index.html', {'form': form})
