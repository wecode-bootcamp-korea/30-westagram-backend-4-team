# Generated by Django 4.0.2 on 2022-02-22 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_user_created_at_alter_user_last_name_and_more'),
        ('postings', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='postings.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='likes', to='users.user')),
            ],
            options={
                'db_table': 'likes',
            },
        ),
    ]
