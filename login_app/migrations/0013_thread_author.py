# Generated by Django 3.1 on 2020-08-30 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0012_auto_20200829_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='author',
            field=models.CharField(max_length=30, null=True, verbose_name='作成者'),
        ),
    ]
