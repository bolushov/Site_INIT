# Generated by Django 5.0.3 on 2024-03-23 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_ads_text_alter_director_text_alter_events_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ads',
            old_name='ads_image',
            new_name='ad_image',
        ),
    ]
