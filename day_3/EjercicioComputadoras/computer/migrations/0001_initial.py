# Generated by Django 4.0.6 on 2022-07-25 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Altavoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(default='Componente', max_length=255)),
                ('marca', models.CharField(max_length=255)),
                ('costo', models.FloatField(default=0)),
                ('stock', models.IntegerField(default=1)),
                ('descripcion', models.CharField(default='Componente', max_length=255)),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Computadora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('cantidad', models.IntegerField(default=1)),
                ('costo', models.FloatField(default=0)),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
                ('altavoz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='computer.altavoz')),
            ],
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(default='Componente', max_length=255)),
                ('marca', models.CharField(max_length=255)),
                ('costo', models.FloatField(default=0)),
                ('stock', models.IntegerField(default=1)),
                ('descripcion', models.CharField(default='Componente', max_length=255)),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(default='Componente', max_length=255)),
                ('marca', models.CharField(max_length=255)),
                ('costo', models.FloatField(default=0)),
                ('stock', models.IntegerField(default=1)),
                ('descripcion', models.CharField(default='Componente', max_length=255)),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True, null=True)),
                ('tamanio', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlacaBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(default='Componente', max_length=255)),
                ('marca', models.CharField(max_length=255)),
                ('costo', models.FloatField(default=0)),
                ('stock', models.IntegerField(default=1)),
                ('descripcion', models.CharField(default='Componente', max_length=255)),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Raton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(default='Componente', max_length=255)),
                ('marca', models.CharField(max_length=255)),
                ('costo', models.FloatField(default=0)),
                ('stock', models.IntegerField(default=1)),
                ('descripcion', models.CharField(default='Componente', max_length=255)),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True, null=True)),
                ('entrada', models.CharField(default='usb', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teclado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(default='Componente', max_length=255)),
                ('marca', models.CharField(max_length=255)),
                ('costo', models.FloatField(default=0)),
                ('stock', models.IntegerField(default=1)),
                ('descripcion', models.CharField(default='Componente', max_length=255)),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True, null=True)),
                ('entrada', models.CharField(default='usb', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='Orden', max_length=255)),
                ('total', models.FloatField(default=0)),
                ('computadoras', models.ManyToManyField(to='computer.computadora')),
            ],
        ),
        migrations.AddField(
            model_name='computadora',
            name='cpu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='computer.cpu'),
        ),
        migrations.AddField(
            model_name='computadora',
            name='monitor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='computer.monitor'),
        ),
        migrations.AddField(
            model_name='computadora',
            name='placabase',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='computer.placabase'),
        ),
        migrations.AddField(
            model_name='computadora',
            name='raton',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='computer.raton'),
        ),
        migrations.AddField(
            model_name='computadora',
            name='teclado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='computer.teclado'),
        ),
    ]
