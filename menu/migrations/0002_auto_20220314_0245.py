# Generated by Django 3.2 on 2022-03-14 02:45

from django.db import migrations
#
from fdwasr_project.settings import BASE_DIR 
from django.core.files import File 
import os



def generate_data_for_menu(apps, schema_editor): 
    """provides initial data for 'menu' model """

    paths = [
        os.path.join(BASE_DIR, 'media/initialimages/menu1.jpg'),
        os.path.join(BASE_DIR, 'media/initialimages/menu2.jpg'),
        os.path.join(BASE_DIR, 'media/initialimages/menu3.jpg'),
        os.path.join(BASE_DIR, 'media/initialimages/menu4.jpg'),
    ]
    count = 0
    for path in paths: 
        with open(path, 'rb') as f: 
            Menu = apps.get_model('menu', 'Menu')
            Menu.objects.create(
                name='Korem, ipsum dolor',
                description='Lorem ipsum dolor sit amet consectetur, adipis antium at cum voluptatem ipsam repudiandae quod.',
                image=File(f, f'menu{count}.jpg'),
                price= count*10 + 12
            )
        count += 1
    

class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(generate_data_for_menu)
    ]
