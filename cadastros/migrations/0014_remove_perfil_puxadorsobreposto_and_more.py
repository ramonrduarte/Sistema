# Generated by Django 4.2 on 2023-05-15 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0013_alter_perfil_encaixe_alter_perfil_encaixepuxador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='puxadorsobreposto',
        ),
        migrations.AddField(
            model_name='perfil',
            name='puxadorsobreposto',
            field=models.ManyToManyField(to='cadastros.puxador'),
        ),
    ]
