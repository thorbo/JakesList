# Generated by Django 3.2.2 on 2021-05-18 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20210518_1542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='cats',
            new_name='category',
        ),
    ]
