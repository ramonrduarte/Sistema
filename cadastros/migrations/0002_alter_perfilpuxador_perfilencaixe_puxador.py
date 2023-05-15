# Generated by Django 4.2 on 2023-04-29 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilpuxador',
            name='perfilencaixe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.modeloperfil', verbose_name='Perfil Encaixe'),
        ),
        migrations.CreateModel(
            name='Puxador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=6, verbose_name='Código')),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Preço')),
                ('acabamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.acabamento')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.modelopuxador')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.tipo')),
            ],
            options={
                'verbose_name': 'Puxador',
                'verbose_name_plural': 'Puxadores',
                'ordering': ['descricao'],
            },
        ),
    ]