from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # The command for listing the columns you want to display (list_display)
    list_display = ["name", "category", "price", "created_on"]

    # Command to create a search bar on top and list the cols you want to search from
    search_fields = ["name", "category", "supplier"]

    # Create a filter on the side, that filters based on those cols.
    list_filter = ["category", "supplier"]

    # Group together relative info on add or update , change the layout of the input fields.
    fieldsets = [
        ["General Information", {
            "fields": ["name", "description", "price", "barcode"]
        }],
        ["Categorization", {
            "fields": ["category", "supplier"]
        }],
    ]