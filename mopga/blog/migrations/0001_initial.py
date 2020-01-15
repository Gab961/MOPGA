# Generated by Django 2.0 on 2020-01-14 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('budget', models.IntegerField()),
                ('note', models.IntegerField()),
            ],
            options={
                'db_table': 'Projet',
            },
        ),
    ]
