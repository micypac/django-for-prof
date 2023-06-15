from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Book, Review


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            username="reviewuser", email="reviewuser@email.com", password="testpass123"
        )

        cls.book = Book.objects.create(
            title="Harry Potter", author="JK Rowling", price="25.00"
        )

        cls.review = Review.objects.create(
            book=cls.book,
            author=cls.user,
            review="An excellent review",
        )

    def test_book_listing(self):
        self.assertEqual(f"{self.book.title}", "Harry Potter")
        self.assertEqual(f"{self.book.author}", "JK Rowling")
        self.assertEqual(f"{self.book.price}", "25.00")

    def test_book_list_view(self):
        resp = self.client.get(reverse("book_list"))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Harry Potter")
        self.assertTemplateUsed(resp, "books/book_list.html")

    def test_book_detail_view(self):
        resp = self.client.get(self.book.get_absolute_url())
        no_resp = self.client.get("/books/12345/")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(no_resp.status_code, 404)
        self.assertContains(resp, "Harry Potter")
        self.assertContains(resp, "An excellent review")
        self.assertTemplateUsed(resp, "books/book_detail.html")
