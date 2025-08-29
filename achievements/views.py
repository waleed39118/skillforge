from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from skills.models import Skill
from .models import Achievement
from .forms import AchievementForm


# Create your views here.
class AchievementCreateView(LoginRequiredMixin, CreateView):
    model = Achievement
    form_class = AchievementForm
    template_name = 'achievements/achievement_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.skill = get_object_or_404(Skill, id=kwargs['skill_id'], user=request.user)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.skill = self.skill
        obj.save()
        return redirect('skills:detail', pk=self.skill.id)
