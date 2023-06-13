from django.shortcuts import render
from django.views.generic import ListView

from .models import Book


class BookListView(ListView):
    model = Book
    # more friendly name. default is 'object_list' in template and contains all objects in the view
    context_object_name = "book_list"
    template_name = "books/book_list.html"
