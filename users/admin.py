from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Unregister the built-in model admin
admin.site.unregister(User)


# Register our own model admin, based on the default UserAdmin
# source1: https://realpython.com/manage-users-in-django-admin/#prevent-non-superusers-from-editing-their-own-permissions
# source2: https://stackoverflow.com/a/60178627/10802391
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    readonly_fields = ['date_joined']
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser']

    def get_fieldsets(self, request, obj=None):
        if not request.user.is_superuser:
            return (
                ('Personal info', {'fields': ('username', 'first_name', 'last_name', 'email')}),
                ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
                ('Important dates', {'fields': ('last_login', 'date_joined')}),
            )
        else:
            return self.fieldsets

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()

        if not is_superuser:
            disabled_fields |= {
                'is_staff',
                'is_superuser',
            }

        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True

        return form
