# Generated by Django 4.0.5 on 2022-07-12 08:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0013_remove_ticket_winning_remove_winningpick_drawing_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='drawing',
            options={'ordering': ('-id',)},
        ),
        migrations.CreateModel(
            name='Mega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('startdate', models.DateTimeField(default=datetime.datetime.now)),
                ('enddate', models.DateTimeField(default=datetime.datetime.now)),
                ('winning_set', models.BooleanField(default=False)),
                ('draw', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mega_draw', to='lottery.drawing')),
            ],
            options={
                'ordering': ('-startdate',),
            },
        ),
        migrations.CreateModel(
            name='Jackpot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('startdate', models.DateTimeField(default=datetime.datetime.now)),
                ('enddate', models.DateTimeField(default=datetime.datetime.now)),
                ('winning_set', models.BooleanField(default=False)),
                ('draw', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jackpot_draw', to='lottery.drawing')),
            ],
            options={
                'ordering': ('-startdate',),
            },
        ),
    ]
