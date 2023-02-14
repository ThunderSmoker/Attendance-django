# Generated by Django 4.1.6 on 2023-02-14 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_student_prn'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batchmate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=200)),
                ('batch', models.CharField(max_length=4)),
                ('prn', models.IntegerField(max_length=20)),
                ('sub', models.CharField(max_length=30)),
                ('present', models.BooleanField(default=False)),
            ],
        ),
    ]