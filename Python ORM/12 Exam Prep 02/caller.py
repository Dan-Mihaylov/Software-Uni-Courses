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


# 05 Django Queries Part-Two
def get_top_products():

    sold_products = (
        Product.objects
        .annotate(count_orders=Count('orders'))
        .filter(count_orders__gt=0)
        .order_by('-count_orders', 'name')[:5]
    )

    result = ["Top products:"] + [
        f"{product.name}, sold {product.count_orders} times"
        for product in sold_products
    ]

    return "\n".join(result) if sold_products else ""


def apply_discounts():

    query = Q(is_completed=False) & Q(count_orders__gt=2)

    orders = (
        Order.objects
        .annotate(count_orders=Count('products'))
        .filter(query)
        .update(total_price=F('total_price') * 0.9)
    )

    return f"Discount applied to {orders} orders."


def complete_order():

    order_to_complete = (
        Order.objects
        .prefetch_related('products')
        .filter(is_completed=False)
        .order_by('creation_date')
        .first()
    )

    if not order_to_complete:
        return ""

    order_to_complete.products.all().update(in_stock=F('in_stock') - 1)

    for product in order_to_complete.products.all():
        if product.in_stock == 0:
            product.is_available = False
            product.save()

    order_to_complete.is_completed = True
    order_to_complete.save()
    return f"Order has been completed!"

