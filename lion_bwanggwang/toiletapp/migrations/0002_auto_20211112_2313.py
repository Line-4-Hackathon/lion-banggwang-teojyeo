# Generated by Django 3.2.4 on 2021-11-12 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toiletapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='toiletapp',
            old_name='pub_datae',
            new_name='pub_date',
        ),
        migrations.RemoveField(
            model_name='toiletapp',
            name='writer',
        ),
    ]