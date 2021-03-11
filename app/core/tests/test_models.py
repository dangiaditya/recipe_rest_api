from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Tests Models """

    def test_create_user_profile_with_email_successful(self):
        """Test Creating a user using an email is successful"""
        email = "test@test.com"
        password = "password123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(email, user.email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "test@Test.com"
        password = "password123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(email.lower(), user.email)

    def test_new_user_invalid_email(self):
        """Test Creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'password123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""

        user = get_user_model().objects.create_superuser(
            email='email@email.com',
            password='password'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
