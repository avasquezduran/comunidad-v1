# Generated by Django 2.2.4 on 2019-09-03 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pagos',
            old_name='cuota',
            new_name='cuotames',
        ),
    ]
