# Generated by Django 3.2.2 on 2021-05-19 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20210518_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='listings',
            name='price',
            field=models.FloatField(),
        ),
    ]
