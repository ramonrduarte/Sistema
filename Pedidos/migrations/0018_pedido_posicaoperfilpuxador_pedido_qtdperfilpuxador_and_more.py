# Generated by Django 4.2 on 2023-07-12 19:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedidos', '0017_alter_pedido_abertura_alter_pedido_data_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='posicaoperfilpuxador',
            field=models.CharField(choices=[('D', 'Direita'), ('E', 'Esquerda'), ('C', 'Cima'), ('B', 'Baixo')], default='1', max_length=10),
        ),
        migrations.AddField(
            model_name='pedido',
            name='qtdperfilpuxador',
            field=models.CharField(default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pedido',
            name='data_pedido',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 12, 16, 52, 41, 543179)),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='linha',
            field=models.CharField(choices=[('Doppio', 'Doppio'), ('1000', '1000')], default='1', max_length=10),
        ),
    ]
