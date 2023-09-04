from  django.core.management.base import BaseCommand

class Command(BaseCommand):

    help = "Print 'hello word' to output."

    def handle(self, *args, **options):
        self.stdout.write('Hello world')