# Generated by Django 2.2.3 on 2019-08-31 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20190829_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='balance',
            field=models.FloatField(default=0.0, max_length=30, verbose_name='Account Balance'),
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]
