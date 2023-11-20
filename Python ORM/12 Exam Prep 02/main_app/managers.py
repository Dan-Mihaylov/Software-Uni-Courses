from django.db.models import Manager, Count


class ProfileManager(Manager):

    def get_regular_customers(self):
        profiles = (self
                    .annotate(order_count=Count('orders'))
                    .filter(order_count__gt=2)
                    .order_by('-order_count')
                    )
        return profiles

