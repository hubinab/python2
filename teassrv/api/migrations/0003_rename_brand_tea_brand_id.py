# Generated by Django 5.1.7 on 2025-04-04 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_tea_brand'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tea',
            old_name='brand',
            new_name='brand_id',
        ),
    ]
