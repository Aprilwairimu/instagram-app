# Generated by Django 4.0.5 on 2022-06-07 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0007_delete_likes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Follow',
        ),
    ]
