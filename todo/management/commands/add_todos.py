from django.core.management.base import BaseCommand

from todo.models import TodoItem


class Command(BaseCommand):
    help = "Add some example todo items to the database"

    def handle(self, *args, **options):
        TodoItem.objects.create(
            title="Say hello",
            description="Introduce everyone to the fantastic possabilities of HTMX",
            done=True,
        )
        TodoItem.objects.create(
            title="Checking boxes",
            description="First thing is first: We'll need to save things to the database\n Without reloading the whole page!",
        )
        TodoItem.objects.create(
            title="Checking boxes part 2",
            description="When we check a box, render the item again so it's crossed out",
        )
        TodoItem.objects.create(
            title="Re-ordering the list do 'done' items are at the bottom",
            description="Let's put `done` items at the bottom of the list when we load the page",
        )
        TodoItem.objects.create(
            title="Re-ordering the list when we check boxes",
            description="Let's put `done` items at the bottom of the list",
        )
        TodoItem.objects.create(
            title="Learn Playwright",
            description="How do we test this thing? Python is not enough!",
        )

        self.stdout.write(self.style.SUCCESS("Added 4 todo items"))
