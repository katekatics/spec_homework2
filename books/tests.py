from django.test import TestCase
from django.urls import reverse

from .models import Book


class BookModelTest(TestCase):
    """
    Тест модели Book
    """

    def setUp(self):
        Book.objects.create(
            title='Война и мир',
            author='Лев Толстой',
            rating=10)

    def tearDown(self):
        Book.objects.all().delete()

    def test_title_in_model(self):
        """
        Проверка на соответсиве поля title модели Book с ожидаемым значением
        """
        book = Book.objects.get(id=1)
        expected_title = 'Война и мир'
        self.assertEqual(book.title, expected_title)


class BookViewTest(TestCase):
    def test_books_url(self):
        """
        Проверка доступности прямой ссылки /books/
        """
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)

    def test_books_url_by_name(self):
        """
        Проверка доступности ссылки по имени 'books'
        """
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)

    def test_books_template(self):
        """
        Проверка отображения корректного шаблона 'books/list.html'
        """
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/list.html')
