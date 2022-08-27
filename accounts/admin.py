from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Información extra', {
                'fields': (
                    'role', 'dni', 'address', 'login_number'),
            }
        )
    )

admin.site.register(User, CustomUserAdmin)
