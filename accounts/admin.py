from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile

# Register the default User model with the built-in UserAdmin
admin.site.unregister(User)  # Optional: only if User is already registered
admin.site.register(User, UserAdmin)

# Register the Profile model
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ('user__username', 'user__email')