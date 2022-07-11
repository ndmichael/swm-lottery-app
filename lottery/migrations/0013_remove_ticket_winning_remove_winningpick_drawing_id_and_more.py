# Generated by Django 4.0.5 on 2022-07-11 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0012_remove_ticket_drawing_id_ticket_bronze_ticket_gold_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='winning',
        ),
        migrations.RemoveField(
            model_name='winningpick',
            name='drawing_id',
        ),
        migrations.AddField(
            model_name='winningpick',
            name='ticket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winning_ticket', to='lottery.ticket'),
        ),
    ]
