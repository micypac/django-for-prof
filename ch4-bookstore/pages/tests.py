from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutPageView


class HomepageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.resp = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.resp, "home.html")

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.resp, "home page")

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.resp, "Hi there! I should not be on the page.")

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("about")
        self.resp = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.resp, "about.html")

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.resp, "About Page")

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.resp, "Hi there! I should not be on the page.")

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve("/about/")
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)
