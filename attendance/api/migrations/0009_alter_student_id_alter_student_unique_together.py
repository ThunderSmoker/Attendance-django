# Generated by Django 4.1.6 on 2023-02-21 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_delete_batchmate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.CharField(editable=False, max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterUniqueTogether(
            name='student',
            unique_together={('prn', 'date')},
        ),
    ]
