# Generated by Django 2.0.5 on 2018-05-12 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('sex', models.CharField(choices=[('N', 'NOT SET'), ('M', 'MAN'), ('W', 'WOMAN'), ('O', 'OTHERS')], default='N', max_length=1)),
                ('birth', models.DateField(verbose_name='Birthday')),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]