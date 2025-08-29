from django import forms
from .models import Skill, SkillProgress

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ('name', 'level', 'started_at')

class SkillProgressForm(forms.ModelForm):
    class Meta:
        model = SkillProgress
        fields = ('percent', 'note')