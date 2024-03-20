from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user
from django.db import IntegrityError
class RegisterTestCase(TestCase):
    
    def test_success_register(self):
        response = self.client.post(
            reverse('users:register'),
            data={
                'username': 'ben',
                'first_name': 'Muhammad',
                'last_name': 'davlatyarov',
                'email': 'm@gmail.com',
                'password': 'ben001',
            } 
        )
        
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)
        
        user = User.objects.get(username='ben')
        self.assertEqual(user.username, 'ben')
        self.assertEqual(user.first_name, 'Muhammad')
        self.assertEqual(user.last_name, 'davlatyarov')
        self.assertEqual(user.email, 'm@gmail.com')
        self.assertTrue(user.check_password, 'ben001')

    # def test_required_fields(self):
    #     response = self.client.post(
    #         reverse('users:register'),
    #         data={
    #             'username': 'ben',
    #             'last_name': 'davlatyarov',
    #             'email': 'm@gmail.com',
    #         }
    #     )
        
    #     form = response.context['form']
    #     self.assertTrue(form.errors)
    #     self.assertEqual(form.errors['username',['this field is required.']])
    #     self.assertEqual(form.errors['password',['this field is required.']])
        
    def test_duplicate_username(self):
        User.objects.create_user(username='ben2', email='ben@gmail.com', password='password1')

        with self.assertRaises(IntegrityError):
            User.objects.create_user(username='ben2', email='anotherben@gmail.com', password='password2')
            
    def test_valid_email(self):
        response = self.client.post(
            reverse('users:register'),
            data={
                'username': 'ben5',
                'first_name': 'Test',
                'last_name': 'User',
                'email': 'test@gmail.com',
                'password': 'password',
            } 
        )
        
        self.assertRedirects(response, reverse('users:login'))  
        
        user_count = User.objects.filter(username='ben5').count()
        self.assertEqual(user_count, 1)
        
        
        
class LoginTestCase(TestCase):
    
    def test_successful_login(self):

        user=User.objects.create_user(username='odam', email='odam@gmail.com', password='password1')
        user.set_password('password1')
        user.save()

        self.client.post(
            reverse('users:login'),  
            data={
                'username': 'odam', 
                'password': 'password1',  
            }
        )

        user = get_user(self.client)
        self.assertTrue(user.is_authenticated)
    
    def test_successful_login(self):
        login_data = {'username': 'user', 'password': 'password123'}
        response = self.client.post(reverse('users:login'), data=login_data)
        self.assertEqual(response.status_code, 200)

        self.assertNotIn('_auth_user_id', self.client.session)
