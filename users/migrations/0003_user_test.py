# Generated by Django 2.2.14 on 2020-07-22 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_auto_20200722_0557"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="test",
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
