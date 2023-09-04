from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Get user by id"

    def add_arguments(self, parser):
        parser.add_argument('id',type=int, help="User_id")

    def handle(self, *args, **kwargs):
        id = kwargs['id']
        users = User.objects.get(id=id)
        self.stdout.write(f'{users}')
