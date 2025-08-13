from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, TemplateView, UpdateView, ListView, DetailView, DeleteView
from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
from .models import Post
from .forms import CreatePostForm, UpdatePostForm

def home_view(request):
    return render(request, 'home.html')

class ListPostView(ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'

class DetailPostView(DetailView):
    model = Post
    template_name = 'blog/view.html'
    context_object_name = 'post'

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/form_create.html'
    form_class = CreatePostForm
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/form_update.html'
    form_class = UpdatePostForm
    context_object_name = 'post'
    success_url = reverse_lazy('posts')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('posts')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user.profile
        return context

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