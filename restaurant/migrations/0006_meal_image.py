# Generated by Django 2.0.7 on 2019-09-01 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_auto_20190901_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='image',
            field=models.ImageField(null=True, upload_to='meals/'),
        ),
    ]