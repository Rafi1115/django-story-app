# Generated by Django 2.2 on 2020-01-11 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0007_post_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='featured',
        ),
    ]