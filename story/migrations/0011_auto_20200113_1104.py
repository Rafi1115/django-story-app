# Generated by Django 2.2 on 2020-01-13 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0010_auto_20200111_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='post',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='story.Category'),
        ),
    ]
