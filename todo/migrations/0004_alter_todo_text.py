# Generated by Django 3.2.4 on 2021-10-02 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20211002_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='text',
            field=models.CharField(max_length=1000),
        ),
    ]
