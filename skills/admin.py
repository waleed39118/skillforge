from django.contrib import admin
from .models import Skill, SkillProgress

# Register your models here.
class SkillProgressInline(admin.TabularInline):
    model = SkillProgress
    extra = 0

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'level', 'started_at', 'updated_at')
    list_filter = ('level',)
    search_fields = ('name', 'user__username')
    inlines = [SkillProgressInline]
