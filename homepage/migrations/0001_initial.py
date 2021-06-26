# Generated by Django 3.2 on 2021-06-22 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('information', models.CharField(max_length=300)),
                ('img', models.ImageField(null=True, upload_to='img/about')),
            ],
        ),
        migrations.CreateModel(
            name='carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headings', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('img', models.ImageField(null=True, upload_to='img/carousel')),
                ('submitted_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(null=True, upload_to='img/client')),
            ],
        ),
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('content', models.CharField(max_length=200, null=True)),
                ('gif', models.FileField(null=True, upload_to='img/services')),
            ],
        ),
    ]
