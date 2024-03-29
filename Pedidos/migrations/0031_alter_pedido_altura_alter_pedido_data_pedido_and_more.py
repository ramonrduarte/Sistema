# Generated by Django 4.2 on 2023-07-26 20:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedidos', '0030_alter_pedido_data_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='altura',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='data_pedido',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 26, 17, 35, 20, 435558)),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='largura',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
    ]
