# Generated by Django 4.2.5 on 2023-09-12 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_role_user_roles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
