# Generated by Django 3.1.7 on 2021-03-30 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='passby',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
