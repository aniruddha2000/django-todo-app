# Generated by Django 2.1 on 2018-11-12 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0002_auto_20181112_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='content',
            field=models.CharField(max_length=20, null=True),
        ),
    ]