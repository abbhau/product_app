# Generated by Django 5.0.3 on 2024-03-31 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='total_prize',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
