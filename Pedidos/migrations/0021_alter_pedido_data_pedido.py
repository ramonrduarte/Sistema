# Generated by Django 4.2 on 2023-07-24 17:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedidos', '0020_alter_pedido_data_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data_pedido',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 24, 14, 3, 55, 475481)),
        ),
    ]