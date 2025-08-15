from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, TemplateView, UpdateView, ListView, DetailView, DeleteView
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
from .models import Post, Comment
from .forms import CreatePostForm, UpdatePostForm, CreateCommentForm, UpdateCommentForm

def home_view(request):
    return render(request, 'blog/home.html')

class ListCommentView(ListView):
    model = Comment
    template_name = 'post/post_detail.html'
    context_object_name = 'comments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        context['post'] = post
        context['comments'] = post.comment_set.all()
        context['form'] = CreateCommentForm()
        return context

class CommentCreateView(CreateView):
    model = Comment
    template_name = 'post/post_detail.html'
    form_class = CreateCommentForm

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.kwargs['pk']})
    
class CommentUpdateView(UpdateView):
    model = Comment
    template_name = 'post/post_detail.html'
    form_class = UpdateCommentForm

    def get_object(self, queryset=None):
        return get_object_or_404(Comment, pk=self.kwargs['comment_pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment = self.get_object()
        post = comment.post
        context['post'] = post
        context['comments'] = post.comment_set.all()
        context['form'] = CreateCommentForm()
        context['editing_comment'] = comment
        return context

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.id})

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'post/post_detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Comment, pk=self.kwargs['comment_pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment = self.get_object()
        post = comment.post
        context['post'] = post
        context['comments'] = post.comment_set.all()
        context['form'] = CreateCommentForm()
        context['deleting_comment'] = comment
        return context

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.id})

class ListPostView(ListView):
    model = Post
    template_name = 'post/list.html'
    context_object_name = 'posts'

class DetailPostView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comment_set.all()
        context['form'] = CreateCommentForm() 
        return context

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post/form_create.html'
    form_class = CreatePostForm
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post/form_update.html'
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
    template_name = 'post/delete.html'
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
    template_name = 'profile/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user.profile
        return context

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'profile/profile_edit.html'

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