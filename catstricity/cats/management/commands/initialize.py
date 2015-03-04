import os
from lxml import etree

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.files import File
from optparse import make_option

from cats.models import Cat

class Command(BaseCommand):
    help = "Prepopulates with some cat photos"
    option_list = BaseCommand.option_list

    def handle(self, *labels, **options):
        xml_file = 'photos/metadata.xml'
        root = etree.parse(open(xml_file))
        database_tag = root.getroot()
        for cat in database_tag.getchildren():
            name = cat.find('name').text
            file = cat.find('file').text
            new_cat = Cat(name=name)
            new_cat.image.save(os.path.basename(file), File(open(file)), save=False)
            new_cat.save()
