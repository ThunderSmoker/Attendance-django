# Generated by Django 4.1.6 on 2023-02-09 18:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Prn',
            new_name='prn',
        ),
        migrations.AddField(
            model_name='student',
            name='batch',
            field=models.CharField(default=datetime.datetime(2023, 2, 9, 18, 14, 27, 799741, tzinfo=datetime.timezone.utc), max_length=4),
            preserve_default=False,
        ),
    ]
