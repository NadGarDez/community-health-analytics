# Generated by Django 5.1.7 on 2025-03-25 17:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostico', '0001_initial'),
        ('doctor', '0003_alter_usuariopersonalizado_apellido_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnostico',
            name='creador',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='doctor.doctor'),
            preserve_default=False,
        ),
    ]
