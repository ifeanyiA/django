# Generated by Django 2.2.3 on 2019-08-03 18:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='title',
        ),
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Publication Date'),
            preserve_default=False,
        ),
    ]
