# Generated by Django 3.2 on 2022-03-13 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactcontent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Contact content',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.PositiveBigIntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=50)),
                ('message', models.TextField(max_length=500)),
                ('sent_on', models.DateField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
            ],
        ),
    ]