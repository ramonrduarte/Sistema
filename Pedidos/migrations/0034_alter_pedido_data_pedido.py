# Generated by Django 4.2 on 2023-08-02 17:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedidos', '0033_alter_pedido_altura_alter_pedido_data_pedido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data_pedido',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 2, 14, 48, 30, 471649)),
        ),
    ]
