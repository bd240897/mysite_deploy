# Generated by Django 3.2.11 on 2022-01-06 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_auto_20220107_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achieve',
            name='certificate',
            field=models.ImageField(blank=True, default='img/achievements/default.jpg', null=True, upload_to='img/achievements/'),
        ),
    ]
