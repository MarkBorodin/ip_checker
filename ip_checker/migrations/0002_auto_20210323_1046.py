# Generated by Django 3.1.7 on 2021-03-23 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ip_checker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ip',
            old_name='number',
            new_name='address',
        ),
    ]
