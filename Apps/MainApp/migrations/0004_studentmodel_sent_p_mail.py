# Generated by Django 2.2 on 2020-10-01 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_auto_20201001_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodel',
            name='sent_p_mail',
            field=models.BooleanField(default=False),
        ),
    ]