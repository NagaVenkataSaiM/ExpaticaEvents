# Generated by Django 3.2.12 on 2022-05-03 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_attendees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendees',
            name='datetime',
            field=models.DateTimeField(null=True),
        ),
    ]
