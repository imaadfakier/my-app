# Generated by Django 3.2 on 2021-10-20 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_restaurant_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='contact',
            field=models.CharField(default='', max_length=10),
        ),
    ]
