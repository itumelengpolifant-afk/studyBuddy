from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    list_display = ("username", "email", "first_name", "last_name", "role", "is_active", "is_staff")
    list_filter = ("role", "is_active", "is_staff")
    search_fields = ("username", "email", "first_name", "last_name")
    ordering = ("username",)

    # Fields shown when editing an existing user
    fieldsets = UserAdmin.fieldsets + (
        ("StudyBuddy role", {"fields": ("role",)}),
    )

    # Fields shown on the "Add user" page
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("StudyBuddy role", {"fields": ("role",)}),
    )