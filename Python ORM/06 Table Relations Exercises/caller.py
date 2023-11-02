import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Book, Artist, Song, Product, Review, Driver, DrivingLicense, Owner, Car, Registration
from datetime import date, timedelta
from django.db.models import Sum, Count


# Create queries within functions


# 01 Author
def show_all_authors_with_their_books() -> str:

    authors = Author.objects.filter(book__isnull=False)

    author_books_information = []

    for author in authors:
        books_information = [f"{book.title}" for book in author.book_set.all()]
        author_books_information.append(f"{author.name} has written - {', '.join(books_information)}!")

    return "\n".join(author_books_information)


def delete_all_authors_without_books() -> None:
    Author.objects.filter(book__isnull=True).delete()


# 02 Music App
def add_song_to_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.add(song)


def get_songs_by_artist(artist_name: str):
    artist = Artist.objects.get(name=artist_name)
    return Song.objects.filter(artists=artist).order_by("-id")
    # By artists you access the artists OBJECTS that are related to the current song Object.
    # In this case we are comparing two Artists instances, in the filter and giving the results in a queryset.


def remove_song_from_artist(artist_name: str, song_title: str) -> None:
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.remove(song)
    # Adding and removing data in a ManyToMany tables is done with the .add / .remove methods. Not .create / .delete


# 03 Shop
def calculate_average_rating_for_product_by_name(product_name: str):
    product = Product.objects.get(name=product_name)

    all_ratings = [review.rating for review in product.reviews.all()]
    return sum(all_ratings) / len(all_ratings)

    # Optimized

    # product = Product.objects.annotate(
    #     total_ratings=Sum('review__rating'),
    #     num_reviews=Count('review')
    # ).get(name=product_name)
    #
    # average_rating = product.total_ratings / product.num_reviews


def get_reviews_with_high_ratings(threshold: int):
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews():
    # product_ids_in_reviews = [review.product_id for review in Review.objects.all()]
    # return Product.objects.exclude(id__in=product_ids_in_reviews).order_by("-name")
    return Product.objects.filter(reviews__isnull=True).order_by("-name")


def delete_products_without_reviews():
    Product.objects.filter(reviews__isnull=True).delete()


# 04 License

def calculate_licenses_expiration_dates():
    licences = DrivingLicense.objects.all().order_by('-license_number')
    expiration_info = [
        f"License with id: {licence.license_number} expires on {licence.issue_date + timedelta(days=365)}!"
        for licence in licences
    ]
    return f"\n".join(expiration_info)


def get_drivers_with_expired_licenses(due_date):

    drivers_expiring_licences = []

    for driver in Driver.objects.all():
        expiring_date = driver.drivinglicense.issue_date + timedelta(days=365)
        if expiring_date > due_date:
            drivers_expiring_licences.append(driver)

    return drivers_expiring_licences

    # Optimized

    # expiration_cutoff_date = due_date - timedelta(days=365)
    #
    # expired_drivers = Driver.objects.filter(drivinglicense__issue_date__gt=expiration_cutoff_date)


# 05 Owner
def register_car_by_owner(owner: Owner):
    registration = Registration.objects.filter(car__isnull=True).first()
    car = Car.objects.filter(registration__isnull=True).first()

    car.owner = owner
    car.save()

    registration.car = car
    registration.registration_date = date.today()
    registration.save()

    return f"Successfully registered {car.model} to {owner.name} with registration number {registration.registration_number}."

