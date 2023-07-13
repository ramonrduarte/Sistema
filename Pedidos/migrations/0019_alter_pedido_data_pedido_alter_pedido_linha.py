# Generated by Django 4.2 on 2023-07-13 16:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedidos', '0018_pedido_posicaoperfilpuxador_pedido_qtdperfilpuxador_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data_pedido',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 13, 13, 44, 45, 725168)),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='linha',
            field=models.CharField(choices=[('Doppio', 'Doppio'), ('Mil', 'Mil')], default='1', max_length=10),
        ),
    ]