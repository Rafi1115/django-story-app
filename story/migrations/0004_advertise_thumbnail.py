# Generated by Django 2.2 on 2019-12-03 13:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0003_advertise'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertise',
            name='thumbnail',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
