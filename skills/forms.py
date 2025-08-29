from django import forms
from .models import Skill, SkillProgress

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ('name', 'level', 'started_at')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-select'}),
            'started_at': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class SkillProgressForm(forms.ModelForm):
    class Meta:
        model = SkillProgress
        fields = ('percent', 'note')