# Generated by Django 3.2.2 on 2021-05-18 21:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20210518_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winning', to=settings.AUTH_USER_MODEL),
        ),
    ]
