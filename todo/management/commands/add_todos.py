from django.core.management.base import BaseCommand

from todo.models import TodoItem


class Command(BaseCommand):
    help = "Add some example todo items to the database"

    def handle(self, *args, **options):
        TodoItem.objects.create(title="Learn HTMX", description="Make a request without writing JavaScript")
        TodoItem.objects.create(title="Learn Alpine.js", description="Add a little interactivity")
        TodoItem.objects.create(title="Learn Tailwind", description="Style things with utility classes")
        TodoItem.objects.create(title="Learn Playwright", description="Write a browser test", done=True)

        self.stdout.write(self.style.SUCCESS("Added 4 todo items"))
