# Generated by Django 4.0.5 on 2022-06-24 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0006_alter_ticket_drawing_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pick',
            name='ball_number',
            field=models.CharField(max_length=50),
        ),
    ]
