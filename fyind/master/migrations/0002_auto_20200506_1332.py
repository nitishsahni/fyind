# Generated by Django 3.0.6 on 2020-05-06 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='engagement',
            field=models.CharField(choices=[('1', '< 6 months'), ('2', '6 to 12 month'), ('3', '12 to 24 months'), ('4', '> 24 months')], max_length=1, verbose_name='Engagement Term'),
        ),
    ]
