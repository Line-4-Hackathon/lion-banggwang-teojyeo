# Generated by Django 3.2.9 on 2021-11-12 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toiletapp', '0004_toiletapp_mainphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toiletapp',
            name='mainphoto',
            field=models.FileField(blank=True, null=True, upload_to='imgs/'),
        ),
    ]