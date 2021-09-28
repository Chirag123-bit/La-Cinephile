from django.test.testcases import TestCase
from halls.models import Hall, Category
from tickets.models import Categories


#Testing Models
class TestModels(TestCase): 
    def setUp(self): #set up required objects for testing
        self.cat = Category.objects.create(
            name="test",
            price=1000,
            color_code = "#fff"
        )

    def test_hall(self):
        """For this test, a hall object is created and checked if its successfully saved in database"""
        hall = Hall.objects.create(
            name="TestHall",
            category = self.cat

        )
        self.assertIsNotNone(Hall.objects.filter(name="TestHall"))

    def test_categories(self):
        """For this test, a category object is created and checked if it's saved in database"""
        cat = Categories.objects.create(
            name="TestCategory",
            discount = 500

        )
        self.assertIsNotNone(Categories.objects.filter(name="TestCategory"))