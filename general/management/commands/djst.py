from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):

    def django_start(self):
        os.system("python manage.py makemigrations")
        os.system("python manage.py migrate")
        os.system("python manage.py runserver")

    def handle(self, *args, **options):
        self.django_start()
        pass
