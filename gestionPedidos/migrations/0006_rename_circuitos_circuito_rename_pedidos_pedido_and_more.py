# Generated by Django 4.2.1 on 2023-06-24 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0005_rename_nombre_circuitos_lugar'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Circuitos',
            new_name='Circuito',
        ),
        migrations.RenameModel(
            old_name='Pedidos',
            new_name='Pedido',
        ),
        migrations.RenameModel(
            old_name='Viajeros',
            new_name='Viajero',
        ),
    ]
