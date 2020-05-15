from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ Test creating a new user with an email is successful"""
        email = 'test@himelrana-swe.com'
        password = 'Testpass123'
        username = 'himeluser'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            username=username,
            first_name='Himel',
            last_name='Rana'
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.first_name, 'Himel')
        self.assertEqual(user.last_name, 'Rana')
        print('FullName is ', user.get_full_name())
        print('Username is: ', user.get_username())
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test the email for a new user is normalized """
        email = 'test@HIMELRANA-SWE.COM'
        user = get_user_model().objects.create_user(email, 'user1', 'test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test Creating user with no email raises error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """ Test Creating new super user """
        user = get_user_model().objects.create_superuser(
            'admin@himelrana-swe.com',
            'testadmin123'
        )

        self.assertEqual(user.is_superuser, True)
        self.assertEqual(user.is_staff, True)
