# Generated by Django 3.2.12 on 2022-04-30 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventname', models.CharField(max_length=20)),
                ('eventid', models.CharField(max_length=20)),
                ('eventdescription', models.CharField(max_length=1000)),
                ('eventimage', models.CharField(max_length=1000)),
                ('username', models.CharField(max_length=20)),
                ('eventmode', models.CharField(max_length=20)),
            ],
        ),
    ]
