from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Creaty user"

    def handle(self, *args, **options):

        user = User(name='Jon', email='Mar@uuu.com', password="dhhddd", age=5)
        user.save()
        self.stdout.write(f'{user}')
