from _decimal import Decimal
from django.db.models import Manager
from django.db.models import Count, Avg


# 01
class RealEstateListingManager(Manager):

    def by_property_type(self, property_type: str):
        return self.filter(property_type=property_type)

    def in_price_range(self, min_price: Decimal, max_price: Decimal):
        return self.filter(price__range=[min_price, max_price])

    def with_bedrooms(self, bedrooms_count: int):
        return self.filter(bedrooms=bedrooms_count)

    def popular_locations(self):

        return self.values("location").annotate(count=Count("location")).order_by("id")[:2]


# 02
class VideoGameManager(Manager):

    def games_by_genre(self, genre: str):
        return self.filter(genre=genre)

    def recently_released_games(self, year: int):
        return self.filter(release_year__gte=year)

    def highest_rated_game(self):
        return self.order_by("-rating").first()

    def lowest_rated_game(self):
        return self.order_by("rating").first()

    def average_rating(self):
        average_rating = self.values('rating').annotate(average=Avg("rating")).order_by("-average")
        result = []
        for rating in average_rating:
            result.append(round(rating["average"], 1))

        return round(sum(result) / len(result), 1)
