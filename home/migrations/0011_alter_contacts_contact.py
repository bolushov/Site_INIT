# Generated by Django 5.0.3 on 2024-03-19 11:19

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_aboutus_ads_contacts_director_enrolee_events_news_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='contact',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Контакты'),
        ),
    ]
