# Generated by Django 4.2 on 2023-05-13 12:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedidos', '0002_alter_pedido_data_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data_pedido',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 13, 9, 46, 32, 749157)),
        ),
    ]
