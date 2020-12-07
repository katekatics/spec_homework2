from django.test import TestCase
from django.urls import reverse


class StoreViewTest(TestCase):
    def test_home_url(self):
        """
        Проверка доступности прямой ссылки /
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_url_by_name(self):
        """
        Проверка доступности ссылки по имени 'home'
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_journals_template(self):
        """
        Проверка отображения корректного шаблона 'base.html'
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
