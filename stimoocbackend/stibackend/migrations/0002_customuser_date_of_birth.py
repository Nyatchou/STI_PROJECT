# Generated by Django 3.1.5 on 2021-02-01 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stibackend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
