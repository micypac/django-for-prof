from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="spiderman", email="peter_parker@email.com", password="spiderman01"
        )

        self.assertEqual(user.username, "spiderman")
        self.assertEqual(user.email, "peter_parker@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="ironman", email="tony_stark@email.com", password="ironman01"
        )

        self.assertEqual(admin_user.username, "ironman")
        self.assertEqual(admin_user.email, "tony_stark@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
