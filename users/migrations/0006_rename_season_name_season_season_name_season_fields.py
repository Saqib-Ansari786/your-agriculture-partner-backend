# Generated by Django 4.2.4 on 2023-09-29 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_remove_field_field_type_remove_field_season"),
    ]

    operations = [
        migrations.RenameField(
            model_name="season", old_name="Season_name", new_name="season_name",
        ),
        migrations.AddField(
            model_name="season",
            name="fields",
            field=models.ManyToManyField(related_name="seasons", to="users.field"),
        ),
    ]
