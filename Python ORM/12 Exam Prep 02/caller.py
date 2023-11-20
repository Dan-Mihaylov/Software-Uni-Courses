import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Profile, Product, Order
from django.db.models import Q, F, Count


# 04 Django Queries Part-One
def get_profiles(search_string=None):

    if search_string is None:
        return ""

    query = (
        Q(full_name__icontains=search_string) |
        Q(email__icontains=search_string) |
        Q(phone_number__icontains=search_string)
    )

    profiles = Profile.objects.filter(query).order_by('full_name')

    found_profiles = "\n".join(
        f"Profile: {profile.full_name},"
        f" email: {profile.email},"
        f" phone number: {profile.phone_number},"
        f" orders: {profile.orders.count()}"
        for profile in profiles
    )

    return found_profiles if profiles else ""


def get_loyal_profiles():

    loyal_profiles = Profile.objects.get_regular_customers()

    if not loyal_profiles:
        return ""

    return f"\n".join(f'Profile: {profile.full_name}, orders: {profile.orders.count()}' for profile in loyal_profiles)


def get_last_sold_products():

    last_sold_order = Order.objects.prefetch_related("products").order_by("-creation_date").first()

    if not last_sold_order:
        return ""

    last_sold_products = (
        f"Last sold products: "
        f"{', '.join(product.name for product in last_sold_order.products.all().order_by('name'))}"
        )

    return last_sold_products



