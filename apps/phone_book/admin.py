from django.contrib import admin
from apps.phone_book.models import Contact

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=["name","address","phone","created_ts", "updated_ts"]