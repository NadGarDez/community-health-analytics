# Generated by Django 5.1.7 on 2025-03-20 17:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centro_medico', '0001_initial'),
        ('consulta', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conducta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('detalle', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='consulta',
            name='PS',
            field=models.TextField(choices=[('P', 'Primaria'), ('S', 'Sucesiva')], default='P', max_length=1),
        ),
        migrations.AddField(
            model_name='consulta',
            name='centro_medico',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='centro_medico.centromedico'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consulta',
            name='conducta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='consulta.conducta'),
            preserve_default=False,
        ),
    ]
