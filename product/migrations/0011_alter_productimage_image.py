# Generated by Django 5.1.7 on 2025-04-14 04:24

import product.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='products/images/', validators=[product.validators.validate_file_size]),
        ),
    ]
