# Generated by Django 2.2 on 2020-01-16 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200116_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projet',
            name='budget',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='projet',
            name='financement_en_cours',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
