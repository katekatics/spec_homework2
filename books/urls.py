from django.urls import path

from .views import BookView, BookDetailView, BookReversedView, BookCreateView, BookEditView, BookDeleteView


urlpatterns = [
    path('', BookView.as_view(), name='books'),
    path('<int:pk>/', BookDetailView.as_view(), name='detail_book'),
    path('books_reversed/', BookReversedView.as_view(), name='books_reversed'),
    path('new/', BookCreateView.as_view(), name='new_book'),
    path('<int:pk>/edit/', BookEditView.as_view(), name='edit_book'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='delete_book')
]
