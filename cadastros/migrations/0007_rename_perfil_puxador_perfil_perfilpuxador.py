# Generated by Django 4.2 on 2023-06-26 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0006_alter_divisor_codigo_alter_divisoriaambiente_codigo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='perfil_puxador',
            new_name='perfilpuxador',
        ),
    ]
