# Generated by Django 2.2.4 on 2019-09-03 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0005_auto_20190903_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagos',
            name='fechapago',
            field=models.DateTimeField(auto_now_add=True, verbose_name='fecha pago'),
        ),
    ]
