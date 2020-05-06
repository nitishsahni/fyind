from django.forms import ModelForm
from django.shortcuts import render
from crispy_forms.helper import FormHelper
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
        if form.is_valid():
            application = form.save(commit=False)
            #get the multiselect date here
        else:
            form = Form()
    context = {'form': form}
    return render(request, 'index.html', context)