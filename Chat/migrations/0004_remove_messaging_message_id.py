# Generated by Django 2.2.3 on 2019-08-01 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0003_remove_user_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messaging',
            name='message_id',
        ),
    ]