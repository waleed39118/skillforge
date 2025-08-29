# accounts/views.py
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import SignUpForm, ProfileForm, UserUpdateForm
from .models import Profile

class SignInView(LoginView):
    template_name = 'accounts/login.html'

class SignOutView(LogoutView):
    next_page = 'login'

class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
            first_name=form.cleaned_data.get('first_name', ''),
            last_name=form.cleaned_data.get('last_name', ''),
        )
        Profile.objects.create(user=user)
        login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('dashboard')

@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = self.request.user
        ctx['user_form'] = UserUpdateForm(instance=user)
        ctx['profile_form'] = ProfileForm(instance=user.profile)
        return ctx

    def post(self, request, *args, **kwargs):
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        return self.get(request, *args, **kwargs)