from django.contrib import admin
from .models import Goal

# Register your models here.
@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'skill', 'status', 'due_date', 'created_at')
    list_filter = ('status',)
    search_fields = ('title', 'skill__name', 'skill__user__username')
