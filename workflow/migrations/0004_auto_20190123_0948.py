# Generated by Django 2.0.7 on 2019-01-23 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0003_workflowteam_team_uuid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coreuser',
            options={'ordering': ('user__first_name',)},
        ),
        migrations.RemoveField(
            model_name='coreuser',
            name='filter',
        ),
        migrations.RemoveField(
            model_name='coreuser',
            name='name',
        ),
    ]
