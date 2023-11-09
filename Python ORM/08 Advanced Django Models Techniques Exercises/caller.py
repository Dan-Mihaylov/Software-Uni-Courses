import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Customer, Book, Product, DiscountedProduct, Hero, FlashHero, SpiderHero, Document
from django.core.exceptions import ValidationError
from decimal import Decimal
from django.contrib.postgres.search import SearchVector

# 04 SuperHero Inputs
# # Create instance of SpiderHero
# spiderman = SpiderHero(name="Spider-Man", hero_title="Spider Hero", energy=100)
# # Create instance of FlashHero
# flash = FlashHero(name="The Flash", hero_title="Flash Hero", energy=70)
#
# # Save the instances to the database
# spiderman.save()
# flash.save()
#
# # Run the special abilities
# print(spiderman.swing_from_buildings())
# print(flash.run_at_super_speed())
# print(spiderman.swing_from_buildings())
#
# # Recharge the energy of Spider-Man and The Flash using the mixin method
# spiderman.recharge_energy(195)
# flash.recharge_energy(40)
#
# # Now you can check the updated energy levels
# print(f"{spiderman.name} - Energy: {spiderman.energy}")
# print(f"{flash.name} - Energy: {flash.energy}")
#
#
# # 05 Document (Search Vector Field)
#
# # Create the first 'Document' object with a title and content.

# document1 = Document.objects.create(
#     title="Bango 1000",
#     content="Django is very very bango web framework.",
# )
#
# # Create the second 'Document' object with a title and content.
# document2 = Document.objects.create(
#     title="Bango 2000",
#     content="Django is not very bango framework web.",
# )
#
# # Update the 'search_vector' field in the 'Document' model with search vectors.
# Document.objects.update(search_vector=SearchVector('title', 'content'))
#
# # Perform a full-text search for documents containing the words 'django' and 'web framework'.
# results = Document.objects.filter(search_vector='django web framework')
#
# # Print the search results.
# for result in results:
#     print(f"Title: {result.title}")
