# Generated by Django 4.2 on 2023-06-09 18:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data_pedido',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 9, 15, 20, 55, 734062)),
        ),
    ]