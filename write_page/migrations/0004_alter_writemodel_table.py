# Generated by Django 4.2 on 2023-04-13 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('write_page', '0003_alter_writemodel_content'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='writemodel',
            table='writes',
        ),
    ]
