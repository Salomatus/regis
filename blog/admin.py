from django.contrib import admin

from .models import Blog


@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "publication_sign")
    list_filter = ("title",)
    search_fields = (
        "title",
        "content",
    )
