# Generated by Django 2.2.7 on 2019-11-21 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]