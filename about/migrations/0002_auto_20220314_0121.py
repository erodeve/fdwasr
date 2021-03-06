# Generated by Django 3.2 on 2022-03-14 01:57

from django.db import migrations
#
from django.core.files import File 
from django.conf import settings
import os


# initial data for 'About' model
def generateDataForAbout(apps, schema_editor): 
    path_to_image = os.path.join(settings.BASE_DIR, 'media/initialimages/team.jpg')
    print('******************')
    print(settings.BASE_DIR)
    with open(path_to_image, 'rb') as f: 

        About = apps.get_model('about', 'About')
        About.objects.create(
            title='Dolor sit amet odit',
            content='Lorem ipsum dolorabo culpa natus dolore! Soluta dolor corporis eos verore perferendis consequuntur',
            image=File(f, 'tema.jpg'),
        )



class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(generateDataForAbout)
    ]
