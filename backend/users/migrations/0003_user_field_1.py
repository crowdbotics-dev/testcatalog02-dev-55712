# Generated by Django 2.2.28 on 2023-01-10 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20230110_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='field_1',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
