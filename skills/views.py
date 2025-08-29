from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, FormView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Skill, SkillProgress
from .forms import SkillForm, SkillProgressForm
from utils.pdf import build_user_report



# Create your views here.
# Web views
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

class SkillListView(LoginRequiredMixin, ListView):
    template_name = 'skills/skills_list.html'
    context_object_name = 'skills'

    def get_queryset(self):
        return Skill.objects.filter(user=self.request.user)

class SkillDetailView(LoginRequiredMixin, DetailView):
    template_name = 'skills/skill_detail.html'
    context_object_name = 'skill'

    def get_queryset(self):
        return Skill.objects.filter(user=self.request.user)

class SkillCreateView(LoginRequiredMixin, CreateView):
    model = Skill
    form_class = SkillForm
    template_name = 'skills/skill_form.html'
    success_url = reverse_lazy('skills:list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return redirect(self.success_url)

class SkillUpdateView(LoginRequiredMixin, UpdateView):
    model = Skill
    form_class = SkillForm
    template_name = 'skills/skill_form.html'
    success_url = reverse_lazy('skills:list')

    def get_queryset(self):
        return Skill.objects.filter(user=self.request.user)

class SkillProgressCreateView(LoginRequiredMixin, FormView):
    form_class = SkillProgressForm
    template_name = 'skills/progress_form.html'

    def form_valid(self, form):
        skill_id = self.kwargs.get('pk')
        skill = Skill.objects.filter(user=self.request.user, id=skill_id).first()
        if not skill:
            return redirect('skills:list')
        progress = form.save(commit=False)
        progress.skill = skill
        progress.save()
        return redirect('skills:detail', pk=skill.id)

class ReportDownloadView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        pdf = build_user_report(request.user)
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="skillforge_report.pdf"'
        return response

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

class SkillListView(LoginRequiredMixin, ListView):
    template_name = 'skills/skills_list.html'
    context_object_name = 'skills'

    def get_queryset(self):
        return Skill.objects.filter(user=self.request.user)

class SkillDetailView(LoginRequiredMixin, DetailView):
    template_name = 'skills/skill_detail.html'
    context_object_name = 'skill'

    def get_queryset(self):
        return Skill.objects.filter(user=self.request.user)

class SkillCreateView(LoginRequiredMixin, CreateView):
    model = Skill
    form_class = SkillForm
    template_name = 'skills/skill_form.html'
    success_url = reverse_lazy('skills:list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return redirect(self.success_url)

class SkillUpdateView(LoginRequiredMixin, UpdateView):
    model = Skill
    form_class = SkillForm
    template_name = 'skills/skill_form.html'
    success_url = reverse_lazy('skills:list')

    def get_queryset(self):
        return Skill.objects.filter(user=self.request.user)

class SkillProgressCreateView(LoginRequiredMixin, FormView):
    form_class = SkillProgressForm
    template_name = 'skills/progress_form.html'

    def form_valid(self, form):
        skill_id = self.kwargs.get('pk')
        skill = Skill.objects.filter(user=self.request.user, id=skill_id).first()
        if not skill:
            return redirect('skills:list')
        progress = form.save(commit=False)
        progress.skill = skill
        progress.save()
        return redirect('skills:detail', pk=skill.id)

class ReportDownloadView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        pdf = build_user_report(request.user)
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="skillforge_report.pdf"'
        return response
