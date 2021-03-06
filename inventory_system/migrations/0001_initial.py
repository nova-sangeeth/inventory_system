# Generated by Django 3.0.2 on 2020-01-23 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='desktops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=256)),
                ('price', models.IntegerField()),
                ('brand', models.CharField(max_length=256, null=True)),
                ('status', models.CharField(default='SOLD', max_length=100)),
                ('issues', models.CharField(default='No issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='headphones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=256)),
                ('price', models.IntegerField()),
                ('brand', models.CharField(max_length=256, null=True)),
                ('status', models.CharField(default='SOLD', max_length=100)),
                ('issues', models.CharField(default='No issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='laptops',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=256)),
                ('price', models.IntegerField()),
                ('brand', models.CharField(max_length=256, null=True)),
                ('status', models.CharField(default='SOLD', max_length=100)),
                ('issues', models.CharField(default='No issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='smartphones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=256)),
                ('price', models.IntegerField()),
                ('brand', models.CharField(max_length=256, null=True)),
                ('status', models.CharField(default='SOLD', max_length=100)),
                ('issues', models.CharField(default='No issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
