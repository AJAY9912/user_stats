from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Role


class UserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("email", "is_staff", "status",)
    list_filter = ("email", "is_staff", "status",)
    fieldsets = (
        (None, {"fields": ("email", "password", "roles")}),
        ("Permissions", {"fields": ("is_staff", "status", "groups", "user_permissions")}),
    )
    raw_id_fields = ["roles"]
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "status", "groups", "user_permissions",
            )}
         ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(User, UserAdmin)
admin.site.register(Role)

