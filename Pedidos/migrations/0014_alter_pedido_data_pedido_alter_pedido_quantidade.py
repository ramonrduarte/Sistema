# Generated by Django 4.2 on 2023-07-03 13:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedidos', '0013_alter_pedido_options_alter_pedido_data_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data_pedido',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 3, 10, 14, 35, 645786)),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='quantidade',
            field=models.CharField(default=1, max_length=2),
        ),
    ]