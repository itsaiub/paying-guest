# Generated by Django 3.1.4 on 2020-12-20 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='listing',
            new_name='couch',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='listing_id',
            new_name='couch_id',
        ),
    ]
