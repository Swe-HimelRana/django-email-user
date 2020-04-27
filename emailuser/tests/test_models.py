from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ Test creating a new user with an email is successful"""
        email = 'test@himelrana-swe.com'
        password = 'Testpass123'
        username = 'himel'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            username=username
        )
        self.assertEqual(user.email, email)
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
