# Generated by Django 3.0.2 on 2020-01-30 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_system', '0002_auto_20200124_0747'),
    ]

    operations = [
        migrations.AddField(
            model_name='desktops',
            name='shipping',
            field=models.CharField(choices=[('SHIPPABLE', 'item can be shipped'), ('NON-SHIPPABLE', 'item cannot be shipped'), ('SPECIAL-SHIPPING', 'item will be shipped late')], default='SHIPPABLE', max_length=100),
        ),
        migrations.AddField(
            model_name='headphones',
            name='shipping',
            field=models.CharField(choices=[('SHIPPABLE', 'item can be shipped'), ('NON-SHIPPABLE', 'item cannot be shipped'), ('SPECIAL-SHIPPING', 'item will be shipped late')], default='SHIPPABLE', max_length=100),
        ),
        migrations.AddField(
            model_name='laptops',
            name='shipping',
            field=models.CharField(choices=[('SHIPPABLE', 'item can be shipped'), ('NON-SHIPPABLE', 'item cannot be shipped'), ('SPECIAL-SHIPPING', 'item will be shipped late')], default='SHIPPABLE', max_length=100),
        ),
        migrations.AddField(
            model_name='smartphones',
            name='shipping',
            field=models.CharField(choices=[('SHIPPABLE', 'item can be shipped'), ('NON-SHIPPABLE', 'item cannot be shipped'), ('SPECIAL-SHIPPING', 'item will be shipped late')], default='SHIPPABLE', max_length=100),
        ),
    ]
