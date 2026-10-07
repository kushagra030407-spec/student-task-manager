from datetime import date, timedelta
from django.core.management.base import BaseCommand
from tasks.models import Task

class Command(BaseCommand):
    help = "Create a small set of sample tasks for the class demonstration."

    def handle(self, *args, **options):
        samples = [
            {
                "title": "Complete Python lab record",
                "description": "Finish the remaining programs and attach their outputs.",
                "due_date": date.today() + timedelta(days=2),
                "priority": "high",
                "completed": False,
            },
            {
                "title": "Revise Django MVT architecture",
                "description": "Review models, views, templates, URLs, and migrations for the viva.",
                "due_date": date.today() + timedelta(days=4),
                "priority": "medium",
                "completed": False,
            },
            {
                "title": "Prepare project README",
                "description": "Document setup steps and explain how to run the application.",
                "due_date": date.today() - timedelta(days=1),
                "priority": "low",
                "completed": True,
            },
        ]
        created = 0
        for item in samples:
            _, was_created = Task.objects.get_or_create(title=item["title"], defaults=item)
            created += int(was_created)
        self.stdout.write(self.style.SUCCESS(f"Sample data ready. Added {created} new task(s)."))
