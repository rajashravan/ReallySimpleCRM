# Generated by Django 3.0.5 on 2020-04-24 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20200418_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
