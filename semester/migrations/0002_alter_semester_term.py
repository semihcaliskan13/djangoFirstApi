# Generated by Django 4.2 on 2023-04-23 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semester', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='term',
            field=models.IntegerField(choices=[(0, 'Fall'), (1, 'Spring'), (2, 'Summer')], default=1),
        ),
    ]
