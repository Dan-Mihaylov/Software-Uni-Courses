from django.db.models import Manager


# 01 Available Products
class ProductManager(Manager):

    def available_products(self):
        result = self.filter(is_available=True)
        return result

    def available_products_in_category(self, category_name: str):
        result = self.filter(category__name=category_name, is_available=True)
        return result

