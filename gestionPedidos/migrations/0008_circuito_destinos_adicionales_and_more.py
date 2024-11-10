# Generated by Django 4.2.16 on 2024-11-10 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0007_alter_viajero_direccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='circuito',
            name='destinos_adicionales',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='circuito',
            name='imagen_principal',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='circuito',
            name='imagenes_galeria',
            field=models.TextField(blank=True, null=True),
        ),
    ]