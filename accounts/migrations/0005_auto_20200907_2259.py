# Generated by Django 3.1.1 on 2020-09-07 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200907_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='example',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(default='', max_length=10),
        ),
    ]
