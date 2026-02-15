from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Show these columns in the users list page
    list_display = ("username", "email", "first_name", "last_name", "is_staff")

    # Add your custom fields to the user edit page
    fieldsets = UserAdmin.fieldsets + (
        ("Extra Info", {"fields": ("date_of_birth", "profile_photo")}),
    )

    # Add your custom fields to the "Add user" page in admin
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Extra Info", {"fields": ("date_of_birth", "profile_photo")}),
    )

