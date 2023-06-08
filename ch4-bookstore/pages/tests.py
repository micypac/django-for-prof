from django.test import SimpleTestCase
from django.urls import reverse


class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

    def test_homepage_url_name(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)

    def test_homepage_template(self):
        resp = self.client.get("/")
        self.assertTemplateUsed(resp, "home.html")

    def test_homepage_contains_correct_html(self):
        resp = self.client.get("/")
        self.assertContains(resp, "home page")

    def test_homepage_does_not_contain_incorrect_html(self):
        resp = self.client.get("/")
        self.assertNotContains(resp, "Hi there! I should not be on the page.")
