from datetime import datetime

from django.core.management import BaseCommand
from semin2_app.models import Author


class Command(BaseCommand):
    help = 'Create authors'
    def handle(self, *args, **kwargs):
        for i in range(10):
            author = Author(name=f'name_{i}', surname=f'surname_{i}', email=f'email_{i}@mail.ru',
                            biography='bla_bla_bla', birthday=datetime.now())
            author.save()
        self.stdout.write('authors created')