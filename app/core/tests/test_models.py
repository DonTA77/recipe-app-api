"""
Test for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Tests models"""

    def test_create_user_with_email_successful(self):
        """Tests creating a user with an email is successful"""
        mail = "test@example.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            self,
            email=mail,
            password=password,
        )

        self.assertEqual(user.email, mail)
        self.assertTrue(user.check_password(password))
