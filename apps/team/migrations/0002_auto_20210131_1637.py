# Generated by Django 3.1.4 on 2021-01-31 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_team_admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='star_counter',
        ),
        migrations.RemoveField(
            model_name='user',
            name='team',
        ),
        migrations.CreateModel(
            name='UserTeamAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_team_admin', models.BooleanField(default=False, verbose_name='is team admin')),
                ('star_counter', models.IntegerField(default=0, verbose_name='star counter')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
