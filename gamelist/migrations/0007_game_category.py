# Generated by Django 2.0.1 on 2018-02-16 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamelist', '0006_auto_20180206_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='category',
            field=models.CharField(choices=[('OTHER', 'Other'), ('ACTION', 'Action'), ('ARCADE', 'Arcade'), ('PUZZLE', 'Puzzle'), ('RACING', 'Racing'), ('SHOOTER', 'Shooter'), ('STRATEGY', 'Strategy')], default='OTHER', max_length=25),
        ),
    ]
