# Generated by Django 4.0.2 on 2022-02-23 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('posted_image', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'posts',
            },
        ),
    ]
