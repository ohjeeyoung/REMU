# Generated by Django 3.1.2 on 2020-10-23 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='images/base_img.jpeg', null=True, upload_to='images/'),
        ),
    ]