# Generated by Django 3.1 on 2020-09-11 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0005_auto_20200911_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='response_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
