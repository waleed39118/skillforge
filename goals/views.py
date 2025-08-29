from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from skills.models import Skill
from .models import Goal
from .forms import GoalForm


# Create your views here.
class GoalCreateView(LoginRequiredMixin, CreateView):
    model = Goal
    form_class = GoalForm
    template_name = 'goals/goal_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.skill = get_object_or_404(Skill, id=kwargs['skill_id'], user=request.user)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.skill = self.skill
        obj.save()
        return redirect('skills:detail', pk=self.skill.id)

class GoalUpdateView(LoginRequiredMixin, UpdateView):
    model = Goal
    form_class = GoalForm
    template_name = 'goals/goal_form.html'

    def get_queryset(self):
        return Goal.objects.filter(skill__user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('skills:detail', kwargs={'pk': self.object.skill.id})
