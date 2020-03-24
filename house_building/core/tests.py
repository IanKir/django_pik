from django.test import TestCase
from core.models import Task, Building


class TaskTestCase(TestCase):
    def setUp(self):
        building = Building.objects.create()
        Task.objects.create(building_number=building, bricks_quantity=500)
        Task.objects.create(building_number=building, bricks_quantity=1000)

    def test_task_creating(self):
        task_1 = Task.objects.get(bricks_quantity=500)
        task_2 = Task.objects.get(bricks_quantity=1000)
        self.assertEqual(task_1.bricks_quantity, 500)
        self.assertEqual(task_2.bricks_quantity, 1000)


class BuildingTestCase(TestCase):
    def setUp(self):
        building_1 = Building.objects.create(title='Дом на Театральной')
        building_2 = Building.objects.create(title='Дом на Пушкинской')
        Task.objects.create(building_number=building_1, bricks_quantity=550)
        Task.objects.create(building_number=building_1, bricks_quantity=116)
        Task.objects.create(building_number=building_2, bricks_quantity=300)
        Task.objects.create(building_number=building_2, bricks_quantity=700)

    def test_building_get_bricks_amount(self):
        building_1_test = Building.objects.get(title='Дом на Театральной')
        building_2_test = Building.objects.get(title='Дом на Пушкинской')
        self.assertEqual(building_1_test.get_bricks_amount(), 666)
        self.assertEqual(building_2_test.get_bricks_amount(), 1000)
