# Generated by Django 4.2 on 2023-06-09 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='divisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cadastros.divisor', verbose_name='Divisor'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='encaixedivisor',
            field=models.CharField(blank=True, choices=[('1', 'Sim'), ('2', 'Não')], max_length=3, null=True),
        ),
    ]
