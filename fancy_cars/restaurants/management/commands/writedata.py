from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Hello')
        filepath = '/Users/michaelmcgill/Python/PythonClass/Django/fancy_cars/fancy_cars/restaurants/management/commands/utilities/recipes.csv'
        data = open(filepath)

        for i in data:
            print(i)
            print(type(i))
            line = i.split(',')
            print(line)
            print(len(line))