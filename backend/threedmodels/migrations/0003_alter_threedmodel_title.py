# Generated by Django 4.2.7 on 2023-11-04 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threedmodels', '0002_file_threedmodel_file_threedmodel_processed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='threedmodel',
            name='title',
            field=models.CharField(max_length=120, verbose_name='Model name'),
        ),
    ]
