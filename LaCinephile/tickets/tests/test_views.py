from django.contrib.auth.models import User
from django import setup
from django.http import response
from django.test.testcases import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.movie_url = reverse('all_movies')
        self.admin_url = reverse('admin_dashboard')
        self.login_url = reverse('login_user')


    def test_categories_GET(self):
        response = self.client.get(self.movie_url)
        
        self.assertEqual(response.status_code, 200) # Assert that we are getting success response on GET requests for this view 
        self.assertTemplateUsed(response, 'movies/movies.html') # Assert that intended template is used by this view

    def test_dashboard_GET(self):
        response = self.client.get(self.admin_url)

        self.assertEqual(response.status_code, 302) #may return 302 code if currently not logged in or logged in as user (redirected)
        # self.assertTemplateUsed(response, 'admins/dashboard.html') # Assert that intended template is used by this view
    
    def test_login_POST(self):
        data = {"username":"HallAdmin", "password":"Abcd@12345"}
        response = self.client.post(self.login_url, data
           )
        self.assertEqual(response.status_code, 200) #validate if the post reqest has succeeded

        
