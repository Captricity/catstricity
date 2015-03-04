import glob
import os

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.files import File
from optparse import make_option

from cats.models import Cat

class Command(BaseCommand):
    help = "Prepopulates with some cat photos"
    option_list = BaseCommand.option_list

    def handle(self, *labels, **options):
        for i, fname in enumerate(glob.glob('photos/*')):
            new_cat = Cat(name='Cat {}'.format(i))
            new_cat.image.save(os.path.basename(fname), File(open(fname, 'r')))
