from django.test.testcases import TestCase
from halls.models import Hall, Category
from tickets.models import Categories

class TestModels(TestCase):
    def setUp(self):
        self.cat = Category.objects.create(
            name="test",
            price=1000,
            color_code = "#fff"
        )

    def test_hall(self):
        
        hall = Hall.objects.create(
            name="TestHall",
            category = self.cat

        )
        self.assertIsNotNone(Hall.objects.filter(name="TestHall"))

    def test_categories(self):
        
        cat = Categories.objects.create(
            name="TestCategory",
            discount = 500

        )
        self.assertIsNotNone(Categories.objects.filter(name="TestCategory"))