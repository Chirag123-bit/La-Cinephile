


from django import setup
from django.http import response
from django.test.testcases import TestCase, Client
from django.urls import reverse
from movies.models import Now_Showing, Up_Comming
import json
from halls.models import Category

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.movie_url = reverse('all_movies')
        self.admin_url = reverse('admin_dashboard')

    def test_categories_GET(self):
        response = self.client.get(self.movie_url)
        
        self.assertEqual(response.status_code, 200) # Assert that we are getting success response on GET requests for this view 
        self.assertTemplateUsed(response, 'movies/movies.html') # Assert that intended template is used by this view

    def test_dashboard_GET(self):
        response = self.client.get(self.admin_url)

        self.assertEqual(response.status_code, 200) #may return 302 code if currently not logged in or logged in as user (redirected)
        self.assertTemplateUsed(response, 'admins/dashboard.html') # Assert that intended template is used by this view
    
    # def test_categories_POST(self):
    #     Category.objects.create(
    #         name = "test",
    #         price = 1000,
    #         color_code = "#fff"
    #     )

    #     response = self.client.post(self.)
