# Generated by Django 5.0.8 on 2024-08-07 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_role_userrole'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(default='USER', max_length=20, unique=True),
        ),
    ]