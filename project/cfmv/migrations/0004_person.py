# Generated by Django 2.2.3 on 2019-08-15 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfmv', '0003_auto_20190815_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('skills', models.CharField(max_length=30)),
            ],
        ),
    ]