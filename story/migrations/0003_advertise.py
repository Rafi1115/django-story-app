# Generated by Django 2.2 on 2019-12-03 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_featuredpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('overview', models.TextField()),
            ],
        ),
    ]
