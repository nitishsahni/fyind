# Generated by Django 3.0.6 on 2020-05-06 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_auto_20200506_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='staff',
            field=models.CharField(choices=[('1', '< 25'), ('2', '25 to 50'), ('3', '51 to 100'), ('4', '> 100')], max_length=1, verbose_name='Number of staff'),
        ),
    ]
