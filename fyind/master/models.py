from django.db import models
from master.choices import *
from django.core.validators import RegexValidator
from multiselectfield import MultiSelectField

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')

class Application(models.Model) :
    nature = models.CharField(max_length=2, choices=nature_choices)
    company_name = models.CharField(verbose_name="Name of Your Company", max_length=100)
    industry = models.CharField(max_length=2, choices=industries_choices)
    country = models.CharField(max_length=2, choices=countries_choices)
    city = models.CharField(max_length=50)
    contact_name = models.CharField(max_length=50, verbose_name="Contact Name")
    email = models.EmailField()
    phone_code = models.CharField(max_length=2, choices=phone_codes_choices, verbose_name="Phone Code")
    phone_number = models.CharField(validators=[phone_regex], max_length=12, verbose_name="Phone Number")
    services = MultiSelectField(choices=services_choices, max_length=500)
    skills = MultiSelectField(choices=skills_choices, max_length=500)
    staff = models.CharField(max_length=1, choices=staff_choices, verbose_name="Number of staff")
    epv = models.CharField(max_length=1, choices=epv_choices, verbose_name="Estimated project value")
    engagement = models.CharField(max_length=1, choices=engagement_choices, verbose_name="Engagement Term")
    urgency = models.CharField(max_length=1, choices=urgency_choices)
    description = models.TextField(max_length=1200, null=True, blank=True)
    status = models.CharField(max_length=2, choices=status_choices, default="IP")

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.company_name
