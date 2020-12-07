from django.test import TestCase
from django.urls import reverse

from .models import Journal


class JournalModelTest(TestCase):
    """
    Тест модели Journal
    """

    def setUp(self):
        Journal.objects.create(
            title='Vouge',
            editor='Anna Wintour',
            page_count=190)

    def tearDown(self):
        Journal.objects.all().delete()

    def test_title_in_model(self):
        """
        Проверка на соответсиве поля editor модели Journal с ожидаемым значением
        """
        journal = Journal.objects.get(id=1)
        expected_editor = 'Anna Wintour'
        self.assertEqual(journal.editor, expected_editor)


class JournalViewTest(TestCase):
    def test_journals_url(self):
        """
        Проверка доступности прямой ссылки /journals/
        """
        response = self.client.get('/journals/')
        self.assertEqual(response.status_code, 200)

    def test_journals_url_by_name(self):
        """
        Проверка доступности ссылки по имени 'journals'
        """
        response = self.client.get(reverse('journals'))
        self.assertEqual(response.status_code, 200)

    def test_journals_template(self):
        """
        Проверка отображения корректного шаблона 'journals/list.html'
        """
        response = self.client.get('/journals/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'journals/list.html')
