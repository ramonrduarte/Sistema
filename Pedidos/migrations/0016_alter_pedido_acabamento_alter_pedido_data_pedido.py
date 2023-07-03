# Generated by Django 4.2 on 2023-07-03 13:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0007_rename_perfil_puxador_perfil_perfilpuxador'),
        ('Pedidos', '0015_alter_pedido_acabamento_alter_pedido_data_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='acabamento',
            field=models.ForeignKey(default='1', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cadastros.acabamento'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='data_pedido',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 3, 10, 18, 51, 104184)),
        ),
    ]
