# Generated by Django 5.1.4 on 2025-01-20 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('PROCESSED', 'Processed'), ('FAILED', 'Failed')], default='PENDING', max_length=10),
        ),
    ]
