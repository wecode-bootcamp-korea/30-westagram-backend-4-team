# Generated by Django 4.0.2 on 2022-02-17 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_name_userinformation_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=100, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'userinfos',
            },
        ),
        migrations.DeleteModel(
            name='UserInformation',
        ),
    ]
