# Generated by Django 2.2.3 on 2019-08-01 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=250)),
                ('album_title', models.CharField(max_length=250)),
                ('artist', models.CharField(max_length=200)),
                ('songs', models.CharField(max_length=200)),
            ],
        ),
    ]
