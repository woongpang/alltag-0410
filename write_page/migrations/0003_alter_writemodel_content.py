# Generated by Django 4.2 on 2023-04-13 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('write_page', '0002_writemodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writemodel',
            name='content',
            field=models.TextField(max_length=256),
        ),
    ]
