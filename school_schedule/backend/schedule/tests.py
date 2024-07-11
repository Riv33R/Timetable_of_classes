from django.test import TestCase
from .models import Class, Subject, Schedule

class ClassModelTest(TestCase):
    def setUp(self):
        self.class1 = Class.objects.create(name="10A")

    def test_class_name(self):
        self.assertEqual(str(self.class1), "10A")

class SubjectModelTest(TestCase):
    def setUp(self):
        self.subject1 = Subject.objects.create(name="Mathematics")

    def test_subject_name(self):
        self.assertEqual(str(self.subject1), "Mathematics")

class ScheduleModelTest(TestCase):
    def setUp(self):
        self.class1 = Class.objects.create(name="10A")
        self.subject1 = Subject.objects.create(name="Mathematics")
        self.schedule1 = Schedule.objects.create(
            class_name=self.class1,
            subject=self.subject1,
            day_of_week='Monday',
            start_time='09:00:00',
            end_time='10:00:00'
        )

    def test_schedule_creation(self):
        self.assertEqual(str(self.schedule1), "10A - Mathematics - Monday 09:00:00-10:00:00")
