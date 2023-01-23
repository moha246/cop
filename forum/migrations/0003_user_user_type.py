# Generated by Django 3.1.14 on 2023-01-23 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(blank=True, choices=[('Admin', 'Admin'), ('Mentor', 'Mentor'), ('Mentee', 'Mentee'), ('Consortium Member', 'Consortium Member')], default='Mentee', max_length=20, null=True),
        ),
    ]
