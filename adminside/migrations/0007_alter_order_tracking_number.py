# Generated by Django 5.0 on 2024-02-18 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminside', '0006_alter_order_tracking_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='tracking_number',
            field=models.CharField(default='EXWA4d612b6e-971b-4be5-ORDER', max_length=30, unique=True),
        ),
    ]