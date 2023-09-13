from django.test import TestCase, Client
from .models import Item

class mainTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.item = Item.objects.create(
            name='Test',
            amount=100,
            goal_amount=1000,
            category='Pendidikan',
            description='Test'
        )

    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_object_is_exist(self):
        test_object = Item.objects.get(name='Test')
        self.assertEqual(test_object.amount, 100)
        self.assertEqual(test_object.goal_amount, 1000)
        self.assertEqual(test_object.category, 'Pendidikan')
        self.assertEqual(test_object.description, 'Test')
