from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class ProfileViewTest(TestCase):
    def test_profile(self):
        # Регистрация нового пользователя
        register_response = self.client.post(
            reverse('users:register'),
            data={
                'username': 'ben',
                'first_name': 'Muhammad',
                'last_name': 'davlatyarov',
                'email': 'm@gmail.com',
                'password': 'ben001',
            } 
        )

        self.assertEqual(register_response.status_code, 302)  # registratsiya tekshirish uchun

        profile_url = reverse('places:profile') # url

        self.client.login(username='ben', password='ben001') # login qilib ko'rishi

        profile_response = self.client.get(profile_url) #get zapros jo'natadi

        self.assertEqual(profile_response.status_code, 200)

        self.assertContains(profile_response, 'ben') 
        self.assertContains(profile_response, 'Muhammad') 
        self.assertContains(profile_response, 'davlatyarov')
        self.assertContains(profile_response, 'm@gmail.com')
