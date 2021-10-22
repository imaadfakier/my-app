# Generated by Django 3.2 on 2021-10-20 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='contact',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
    ]