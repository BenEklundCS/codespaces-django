# Generated by Django 5.0.9 on 2024-09-29 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestrecord',
            name='temperature',
            field=models.CharField(max_length=100),
        ),
    ]
