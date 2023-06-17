from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Book


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    # more friendly name. default is 'object_list' in template and contains all objects in the view
    context_object_name = "book_list"
    template_name = "books/book_list.html"
    login_url = "account_login"


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    context_object_name = "book"
    template_name = "books/book_detail.html"
    login_url = "account_login"
    permission_required = "books.special_status"
    queryset = Book.objects.all().prefetch_related(
        "reviews__author",
    )


class SearchResultsListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/search_results.html"
    # queryset = Book.objects.filter(title__icontains="beginners")

    def get_queryset(self) -> QuerySet[Any]:
        query = self.request.GET.get("q")
        return Book.objects.filter(
            # Q(title__icontains="beginners") | Q(title__icontains="api")
            Q(title__icontains=query)
            | Q(author__icontains=query)
        )
