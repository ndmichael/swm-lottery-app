# Generated by Django 4.0.5 on 2022-06-30 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0004_ticket_winning'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='winning',
            field=models.OneToOneField(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winning_ticket', to='lottery.winningpick'),
        ),
    ]
