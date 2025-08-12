from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView, UpdateView, ListView
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.urls import reverse_lazy
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'


class CreatePostView(CreateView, LoginRequiredMixin):
    model = Post
    template_name = 'create_post.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.author =self.request.user
        return super().form_valid(form)
        
    
def home_view(request):
    return render(request, 'home.html')


class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'profile_edit.html'

    def get(self, request, *args, **kwargs):
        u_form = UserUpdateForm(instance= request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        return self.render_to_response({
            'u_form': u_form,
            'p_form': p_form
        })
    
    def post(self, request, *args, **kwargs):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile')
        
        return self.render_to_response({
            'u_form': u_form,
            'p_form': p_form
        })