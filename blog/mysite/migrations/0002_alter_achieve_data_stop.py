# Generated by Django 4.0 on 2022-01-02 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achieve',
            name='data_stop',
            field=models.DateField(blank=True),
        ),
    ]
