# Generated by Django 2.0.5 on 2018-05-13 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exp3', '0004_user_follow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='follow',
            field=models.ManyToManyField(blank=True, to='exp3.User'),
        ),
    ]
