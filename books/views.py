from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Book


class BookView(LoginRequiredMixin, ListView):
    """
    Класс для отображения набора книг
    """
    model = Book
    template_name = 'books/list.html'
    context_object_name = 'books'
    login_url = 'login'


class BookDetailView(LoginRequiredMixin, DetailView):
    """
    Класс для детального отображения книги
    """
    model = Book
    template_name = 'books/detail.html'
    context_object_name = 'book'
    login_url = 'login'


class BookReversedView(LoginRequiredMixin, ListView):
    """
    Класс для отображения набора книг, отсортированный
    в порядке убывания рейтинга
    """
    model = Book
    queryset = Book.objects.all().order_by('-rating')
    template_name = 'books/list.html'
    context_object_name = 'books'
    login_url = 'login'


class BookEditView(LoginRequiredMixin, UpdateView):
    """
    Класс для редактирования книги. Поля: title, author, rating
    """
    model = Book
    template_name = "books/edit.html"
    fields = ("title", "author", "rating")
    context_object_name = "book"
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        """
        Метод для проверки прав доступа на возможность редактирования книги
        Редактировать может только тот, кто ее создал
        """
        book_object = self.get_object()
        if book_object.owner != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class BookDeleteView(LoginRequiredMixin, DeleteView):
    """
    Класс для удаления журнала
    """
    model = Book
    template_name = "books/delete.html"
    success_url = reverse_lazy("books")
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        """
        Метод для проверки прав доступа на возможность удаления книги
        Удалять может только тот, кто ее создал
        """
        book_object = self.get_object()
        if book_object.owner != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class BookCreateView(LoginRequiredMixin, CreateView):
    """
    Класс для создания новой книги
    """
    model = Book
    template_name = "books/new.html"
    fields = ("title", "author", "rating")
    login_url = 'login'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
