# Generated by Django 5.1.7 on 2025-04-05 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_remove_review_date_review_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
