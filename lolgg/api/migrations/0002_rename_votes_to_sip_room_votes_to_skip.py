# Generated by Django 5.0.6 on 2024-05-10 23:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="room",
            old_name="votes_to_sip",
            new_name="votes_to_skip",
        ),
    ]
