# Generated by Django 3.1 on 2020-09-10 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0003_auto_20200910_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='response_id',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Response',
        ),
    ]
