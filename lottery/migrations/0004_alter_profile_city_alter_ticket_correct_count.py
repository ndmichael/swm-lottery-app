# Generated by Django 4.0.5 on 2022-06-24 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0003_profile_balance_ticket_ticket_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='correct_count',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
