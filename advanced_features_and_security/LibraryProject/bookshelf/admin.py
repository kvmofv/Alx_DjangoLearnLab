from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'date_of_birth', 'profile_photo')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'date_of_birth', 'profile_photo')}),
    )

    list_display = ['username', 'email', 'role', 'is_staff', 'is_superuser']
    list_filter = ['role', 'is_staff', 'is_superuser']

admin.site.register(CustomUser, CustomUserAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year',)
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)