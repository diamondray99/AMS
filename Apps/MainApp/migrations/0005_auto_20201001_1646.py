# Generated by Django 2.2 on 2020-10-01 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_studentmodel_sent_p_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodel',
            name='sent_a_mail',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='payment_date',
            field=models.DateField(blank=True, help_text='Year-Month-Day', null=True),
        ),
    ]
