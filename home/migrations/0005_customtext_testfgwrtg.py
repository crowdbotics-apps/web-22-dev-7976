# Generated by Django 2.2.14 on 2020-07-22 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_remove_customtext_tests"),
    ]

    operations = [
        migrations.AddField(
            model_name="customtext",
            name="testfgwrtg",
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
