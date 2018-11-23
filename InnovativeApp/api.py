from django.core.management.base import BaseCommand
from to_do_app.models import Task_Details



class Command(BaseCommand):
    help = 'Prints the titles of all Posts'

    def handle(self, *args, **options):
        for post in Task_Details.objects.all():
            print(a.Task_Id)

print('abcd')
sys.path.append('C:\Python1\django\InnovativeApp')
os.environ['DJANGO_SETTINGS_MODULE'] = 'InnovativeApp.settings'
django.setup()
Command()
