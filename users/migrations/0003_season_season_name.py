# Generated by Django 4.2.4 on 2023-09-23 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_season"),
    ]

    operations = [
        migrations.AddField(
            model_name="season",
            name="Season_name",
            field=models.CharField(default="Season", max_length=255),
        ),
    ]