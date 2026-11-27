from django.core.management.base import BaseCommand

from todo.models import TodoItem


class Command(BaseCommand):
    help = "Delete all todo items from the database"

    def handle(self, *args, **options):
        count, _ = TodoItem.objects.all().delete()

        self.stdout.write(self.style.SUCCESS(f"Deleted {count} todo items"))
