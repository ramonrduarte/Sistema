# Generated by Django 4.2 on 2023-07-26 20:23

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedidos', '0028_alter_pedido_altura_alter_pedido_data_pedido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='altura',
            field=models.DecimalField(decimal_places=0, max_digits=4, validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='data_pedido',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 26, 17, 23, 20, 664943)),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='largura',
            field=models.DecimalField(decimal_places=0, max_digits=4, validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(0)]),
        ),
    ]