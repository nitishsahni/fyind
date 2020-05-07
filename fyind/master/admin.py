from django.contrib import admin
from .models import *

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'country', 'contact_name', 'email', 'urgency', 'epv')
    list_filter = ('urgency', 'epv', 'status')
    search_fields = ('company_name', 'contact_name')

admin.site.register(Application, ApplicationAdmin)