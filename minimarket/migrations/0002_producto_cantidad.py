# Generated by Django 4.1.7 on 2023-06-19 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimarket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
    ]