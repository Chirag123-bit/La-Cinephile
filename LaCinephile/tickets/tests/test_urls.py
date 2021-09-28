from django.test import SimpleTestCase
from django.urls import reverse, resolve
from movies.views import movies
from accounts.views import register
from admins.views import admin_profile




class TestUrls(SimpleTestCase):

    def test_all_movies_url_is_resolved(self):
        url = reverse('all_movies') #Store reverse url link of 'all_movie'
        self.assertEqual(resolve(url).func, movies) #Assert that the url is returning the inteneded function

    def test_register_user_url_is_resolved(self):
        url = reverse('register_user') #Store reverse url link of 'register_user'
        self.assertEqual(resolve(url).func, register) #Assert that the url is returning the inteneded function

    def test_show_admin_profile_url_is_resolved(self):
        url = reverse('show_admin_profile')#Store reverse url link of 'show_admin_profile'
        self.assertEqual(resolve(url).func, admin_profile)  #Assert that the url is returning the inteneded function
