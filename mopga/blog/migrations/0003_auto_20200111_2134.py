# Generated by Django 2.0 on 2020-01-11 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200111_1331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='description',
        ),
    ]
