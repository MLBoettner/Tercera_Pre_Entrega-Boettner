# Generated by Django 4.1.6 on 2023-02-12 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudio',
            old_name='entregado',
            new_name='recibido',
        ),
    ]