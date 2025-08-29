from django.contrib import admin
from .models import Achievement

# Register your models here.
@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'skill', 'created_at')
    search_fields = ('title', 'skill__name', 'skill__user__username')
