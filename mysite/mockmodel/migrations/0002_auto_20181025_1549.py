# Generated by Django 2.1.2 on 2018-10-25 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mockmodel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mocktest',
            name='remark',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='mocktest',
            name='server',
            field=models.CharField(default='', max_length=10),
        ),
    ]
