# Generated by Django 4.2.1 on 2023-06-24 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0004_rename_clientes_viajeros'),
    ]

    operations = [
        migrations.RenameField(
            model_name='circuitos',
            old_name='nombre',
            new_name='lugar',
        ),
    ]
