# Generated by Django 4.0.2 on 2022-02-17 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_delete_userinformation'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='members',
        ),
    ]