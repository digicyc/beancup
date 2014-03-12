from django.test import TestCase
from bean.models import Bean, BeanBrand


class BeanTestCase(TestCase):
    def setUp(self):
        brew_brand = BeanBrand.objects.create(name="Aaron Coffee")
        Bean.objects.create(name='Dark Brew', brand=brew_brand,
                            description="Good stuff", dark_level=('M', 'Medium'),
                            price=20.00)

    def test_brand(self):
        bean = Bean.objects.get(name='Dark Brew')
        self.assertEqual(bean.brand.name, "Aaron Coffee")

    def test_bean_name(self):
        bean = Bean.objects.get(name='Dark Brew')
        self.assertEqual(bean.name, 'Dark Brew')

    def test_bean_price(self):
        bean = Bean.objects.get(name='Dark Brew')
        self.assertEqual(bean.price, 20.00)

