# Generated by Django 3.1.14 on 2023-01-23 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("forum", "0003_user_user_type"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="name",
            new_name="username",
        ),
    ]
