from datetime import date
from django.test import TestCase
from django.urls import reverse
from .models import Task

class TaskManagerTests(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title="Test assignment",
            description="A sample task",
            due_date=date(2026, 10, 20),
            priority="high",
        )

    def test_dashboard_loads_and_shows_task(self):
        response = self.client.get(reverse("tasks:dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test assignment")

    def test_create_task(self):
        response = self.client.post(reverse("tasks:task_create"), {
            "title": "New assignment",
            "description": "Created in test",
            "due_date": "",
            "priority": "medium",
        })
        self.assertRedirects(response, reverse("tasks:dashboard"))
        self.assertTrue(Task.objects.filter(title="New assignment").exists())

    def test_toggle_task_completion(self):
        response = self.client.post(reverse("tasks:task_toggle", args=[self.task.pk]))
        self.assertRedirects(response, reverse("tasks:dashboard"))
        self.task.refresh_from_db()
        self.assertTrue(self.task.completed)

    def test_delete_task(self):
        response = self.client.post(reverse("tasks:task_delete", args=[self.task.pk]))
        self.assertRedirects(response, reverse("tasks:dashboard"))
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())
