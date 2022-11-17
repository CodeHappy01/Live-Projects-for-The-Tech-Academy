# Generated by Django 2.2.5 on 2022-11-15 17:35

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CookieJar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Accomplishment', models.TextField(default='')),
            ],
            managers=[
                ('cookies', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='SaveJoke',
            fields=[
                ('Setup', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('Delivery', models.CharField(max_length=200, unique=True)),
            ],
            managers=[
                ('jokes', django.db.models.manager.Manager()),
            ],
        ),
    ]
