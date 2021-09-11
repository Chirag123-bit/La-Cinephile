


from django.test.testcases import TestCase
from tickets.models import Categories

class TestModels(TestCase):
    def setUp(self):
        self.project1 = Categories.objects.create(
            name="Test",
            discount = 1000
        )

    def test_categories(self):
        pass