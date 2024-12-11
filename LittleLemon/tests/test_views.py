from django.test import TestCase
from Restaurant.models import Menu
from Restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.menu1 = Menu.objects.create(title='IceCream', price=80, inventory=100)
        self.menu2 = Menu.objects.create(title='Burger', price=50, inventory=200)
        self.menu3 = Menu.objects.create(title='Pizza', price=100, inventory=150)

    def test_getall(self):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        expected_data = [
            {'id': self.menu1.id, 'title': 'IceCream', 'price': '80.00', 'inventory': 100},
            {'id': self.menu2.id, 'title': 'Burger', 'price': '50.00', 'inventory': 200},
            {'id': self.menu3.id, 'title': 'Pizza', 'price': '100.00', 'inventory': 150}
        ]
        self.assertEqual(serializer.data, expected_data)
