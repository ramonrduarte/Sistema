# Generated by Django 4.2 on 2023-07-13 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0007_rename_perfil_puxador_perfil_perfilpuxador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='divisoriaambiente',
            name='linha',
            field=models.CharField(choices=[('Doppio', 'Doppio'), ('Mil', 'Mil')], max_length=50),
        ),
    ]
