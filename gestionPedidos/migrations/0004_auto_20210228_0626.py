# Generated by Django 3.1.7 on 2021-02-28 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0003_auto_20210228_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='telefono',
            field=models.CharField(max_length=9, verbose_name='Teléfono'),
        ),
    ]