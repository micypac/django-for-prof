from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve


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


class SignUpPageTests(TestCase):
    username = "newuser"
    email = "newuser@email.com"

    def setUp(self):
        url = reverse("account_signup")
        self.resp = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.resp.status_code, 200)
        self.assertTemplateUsed(self.resp, "account/signup.html")
        self.assertContains(self.resp, "Sign Up")
        self.assertNotContains(self.resp, "I should not be on the page.")

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
