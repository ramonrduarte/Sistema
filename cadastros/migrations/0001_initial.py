# Generated by Django 4.2 on 2023-05-16 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acabamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acabamento', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Acabamento',
                'verbose_name_plural': 'Acabamentos',
                'ordering': ['acabamento'],
            },
        ),
        migrations.CreateModel(
            name='ModeloDivisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'verbose_name': 'Modelo Divisor',
                'verbose_name_plural': 'Modelo Divisores',
                'ordering': ['modelo'],
            },
        ),
        migrations.CreateModel(
            name='ModeloDivisoriaAmbiente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'verbose_name': 'Modelo Divisoria Ambiente',
                'verbose_name_plural': 'Modelos Divisorias Ambiente',
                'ordering': ['modelo'],
            },
        ),
        migrations.CreateModel(
            name='ModeloPerfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'verbose_name': 'Modelo Perfil',
                'verbose_name_plural': 'Modelo Perfis',
                'ordering': ['modelo'],
            },
        ),
        migrations.CreateModel(
            name='ModeloPerfilPuxador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'verbose_name': 'Modelo Perfil Puxador',
                'verbose_name_plural': 'Modelo Perfis Puxadores',
                'ordering': ['modelo'],
            },
        ),
        migrations.CreateModel(
            name='ModeloPuxador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'verbose_name': 'Modelo Puxador',
                'verbose_name_plural': 'Modelo Puxadores',
                'ordering': ['modelo'],
            },
        ),
        migrations.CreateModel(
            name='ModeloVidro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'verbose_name': 'Modelo Vidro',
                'verbose_name_plural': 'Modelos Vidros',
                'ordering': ['modelo'],
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=6, unique=True, verbose_name='Código')),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Preço')),
                ('encaixe', models.CharField(blank=True, choices=[('1', 'Sim'), ('2', 'Não')], max_length=3, null=True)),
                ('encaixepuxador', models.CharField(blank=True, choices=[('1', 'Sim'), ('2', 'Não')], max_length=3, null=True)),
                ('acabamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.acabamento')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.modeloperfil')),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfis',
                'ordering': ['descricao'],
            },
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
            ],
            options={
                'verbose_name': 'Puxador',
                'verbose_name_plural': 'Puxadores',
                'ordering': ['descricao'],
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'ordering': ['tipo'],
            },
        ),
        migrations.CreateModel(
            name='Vidro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=6, verbose_name='Código')),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Preço')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.modelovidro')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.tipo')),
            ],
            options={
                'verbose_name': 'Vidro',
                'verbose_name_plural': 'Vidros',
                'ordering': ['descricao'],
            },
        ),
        migrations.CreateModel(
            name='PuxadorIntermediario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perfil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='puxadores_perfil', to='cadastros.perfil')),
                ('puxador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='puxadores_perfil', to='cadastros.puxador')),
            ],
        ),
        migrations.AddField(
            model_name='puxador',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.tipo'),
        ),
        migrations.CreateModel(
            name='PerfilPuxador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=6, verbose_name='Código')),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Preço')),
                ('acabamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.acabamento')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.modeloperfilpuxador')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.tipo')),
            ],
            options={
                'verbose_name': 'Perfil Puxador',
                'verbose_name_plural': 'Perfis Puxadores',
                'ordering': ['descricao'],
            },
        ),
        migrations.AddField(
            model_name='perfil',
            name='perfil_puxador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cadastros.perfilpuxador', verbose_name='Perfil Puxador'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='puxadorsobreposto',
            field=models.ManyToManyField(related_name='puxadores', through='cadastros.PuxadorIntermediario', to='cadastros.puxador'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.tipo'),
        ),
        migrations.CreateModel(
            name='DivisoriaAmbiente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=6, verbose_name='Código')),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Preço')),
                ('linha', models.CharField(choices=[('Doppio', 'Doppio'), ('mil', '1000')], max_length=50)),
                ('posicao', models.CharField(choices=[('Travessa/Inferior', 'Travessa/Inferior'), ('Superior', 'Superior'), ('Lateral', 'Lateral'), ('Superior/Inferior', 'Superior/Inferior'), ('Inferior', 'Inferior'), ('Travessa', 'Travessa')], max_length=50)),
                ('acabamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.acabamento')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.modelodivisoriaambiente')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.tipo')),
            ],
            options={
                'verbose_name': 'Perfil Divisoria Ambiente',
                'verbose_name_plural': 'Perfis Divisorias Ambiente',
                'ordering': ['descricao'],
            },
        ),
        migrations.CreateModel(
            name='Divisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=6, verbose_name='Código')),
                ('descricao', models.CharField(max_length=150, verbose_name='Descrição')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Preço')),
                ('acabamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.acabamento')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.modelodivisor')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.tipo')),
            ],
            options={
                'verbose_name': 'Perfil Divisor',
                'verbose_name_plural': 'Perfis Divisores',
                'ordering': ['descricao'],
            },
        ),
    ]
