# Generated by Django 5.1.7 on 2025-03-29 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0004_alter_consulta_centro_medico_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='tipo',
            field=models.TextField(choices=[('M', 'Morbilidad'), ('C', 'Visita de Campo')], default='M', max_length=1),
        ),
    ]
