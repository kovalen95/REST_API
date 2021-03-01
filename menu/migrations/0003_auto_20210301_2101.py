# Generated by Django 3.1.7 on 2021-03-01 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20210227_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dishes',
            name='menu',
        ),
        migrations.AddField(
            model_name='menu',
            name='dishes',
            field=models.ManyToManyField(to='menu.Dishes'),
        ),
        migrations.AlterField(
            model_name='dishes',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='dishes',
            name='date_uploaded',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='date_uploaded',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
