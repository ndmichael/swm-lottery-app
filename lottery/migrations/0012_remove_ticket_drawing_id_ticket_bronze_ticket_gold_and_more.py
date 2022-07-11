# Generated by Django 4.0.5 on 2022-07-11 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0011_alter_gold_enddate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='drawing_id',
        ),
        migrations.AddField(
            model_name='ticket',
            name='bronze',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bronze_ticket', to='lottery.bronze'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='gold',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gold_ticket', to='lottery.gold'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='platinum',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='platinum_ticket', to='lottery.platinum'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='silver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='silver_ticket', to='lottery.silver'),
        ),
    ]