# Generated by Django 4.2.7 on 2023-11-04 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threedmodels', '0003_alter_threedmodel_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='File',
        ),
    ]