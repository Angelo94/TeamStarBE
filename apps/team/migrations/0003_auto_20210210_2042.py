# Generated by Django 3.1.4 on 2021-02-10 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20210131_1637'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userteamassignment',
            unique_together={('team', 'user')},
        ),
    ]