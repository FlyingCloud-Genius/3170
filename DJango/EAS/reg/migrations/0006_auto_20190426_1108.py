# Generated by Django 2.1.7 on 2019-04-26 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0005_auto_20190425_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegInfo',
            fields=[
                ('reg_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('reg_password', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'reg_info',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Info',
        ),
    ]