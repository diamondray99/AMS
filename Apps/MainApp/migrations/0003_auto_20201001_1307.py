# Generated by Django 2.2 on 2020-10-01 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_studentmodel_payment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='transaction_id',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
