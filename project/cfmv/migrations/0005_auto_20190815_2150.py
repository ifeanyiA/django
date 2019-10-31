# Generated by Django 2.2.3 on 2019-08-15 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfmv', '0004_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='skills',
        ),
        migrations.AddField(
            model_name='person',
            name='skills',
            field=models.ManyToManyField(to='cfmv.DeveloperSkill'),
        ),
    ]