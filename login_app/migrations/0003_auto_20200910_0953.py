# Generated by Django 3.1 on 2020-09-10 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_response'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='posted_at',
            new_name='responsed_at',
        ),
    ]
