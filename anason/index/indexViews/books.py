from django.http import HttpResponse
from django.views.generic import ListView
from index.indexModels import Book

class BookListView(ListView):
    model = Book

    def head(self, *args, **kwargs):
        response = HttpResponse('ENTRA EL LISTA DE LIBROS')
        return response
