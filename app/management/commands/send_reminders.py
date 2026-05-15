from django.core.management.base import BaseCommand
from django.utils import timezone
from app.models import Task
from app.utils import send_deadline_email
import datetime

class Command(BaseCommand):
    help = 'Send email reminders for tasks with upcoming deadlines'

    def handle(self, *args, **kwargs):
        # Find tasks that are not completed and have a deadline tomorrow
        tomorrow = timezone.now().date() + datetime.timedelta(days=1)
        tasks = Task.objects.filter(completed=False, due_date=tomorrow)
        
        self.stdout.write(f"Found {tasks.count()} tasks with deadlines tomorrow.")
        
        for task in tasks:
            if task.user.email:
                success = send_deadline_email(task)
                if success:
                    self.stdout.write(self.style.SUCCESS(f"Sent reminder for task: {task.title} to {task.user.email}"))
                else:
                    self.stdout.write(self.style.ERROR(f"Failed to send reminder for task: {task.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"User {task.user.username} has no email address."))
