# Generated by Django 5.0.3 on 2024-03-23 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_remove_slide_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='title',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Название'),
        ),
    ]
