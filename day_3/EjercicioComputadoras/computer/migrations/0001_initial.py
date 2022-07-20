# Generated by Django 4.0.6 on 2022-07-20 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DispositivoEntrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrada', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tamanio', models.CharField(max_length=255)),
                ('marca', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Raton',
            fields=[
                ('dispositivoentrada_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='computer.dispositivoentrada')),
            ],
            bases=('computer.dispositivoentrada',),
        ),
        migrations.CreateModel(
            name='Teclado',
            fields=[
                ('dispositivoentrada_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='computer.dispositivoentrada')),
            ],
            bases=('computer.dispositivoentrada',),
        ),
        migrations.CreateModel(
            name='Computadora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('monitor', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='computer.monitor')),
                ('orden', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='computer.orden')),
                ('raton', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='computer.raton')),
                ('teclado', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='computer.teclado')),
            ],
        ),
    ]
