# Generated by Django 3.2 on 2022-03-15 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homecontent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('welcomeline', models.CharField(max_length=70)),
                ('menuline', models.CharField(max_length=200)),
                ('titleslideone', models.CharField(max_length=40)),
                ('descriptionslideone', models.TextField(max_length=200)),
                ('titleslidetwo', models.CharField(max_length=40)),
                ('descriptionslidetwo', models.TextField(max_length=200)),
                ('facebooklink', models.URLField()),
                ('youtubelink', models.URLField()),
                ('instagramlink', models.URLField()),
            ],
            options={
                'verbose_name': 'Homecontent',
                'verbose_name_plural': 'Home content',
            },
        ),
    ]
