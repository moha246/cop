# Generated by Django 4.1.5 on 2023-02-17 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_remove_user_forums_user_forum"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="forum",
            new_name="forums",
        ),
    ]