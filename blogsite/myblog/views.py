from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import UserSignupForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post


# Class based views
'''
NOTE: 
Class based views look for templates with the format:
<app>/<model>_<viewtype>.html
'''
class HomePageView(ListView):
    template_name = 'myblog/index.html' 
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(date_published__lte=timezone.now()).order_by('-date_published')[:10]

class PostView(DetailView):
    model = Post

class AuthorPostsView(ListView):
    context_object_name = 'post_list'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(date_published__lte=timezone.now(), author=user).order_by('-date_published')[:10]


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','body','image']
    
    #template_name='myblog/post_form.html'
    # success_url can be used to redirect to a link after post is created

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name='myblog/postform.html'
    fields = ['title','body','image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # UserPassesTestMixin runs this function
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url= '/'

    # UserPassesTestMixin runs this function
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# Function based views

def register(request):
    
    if request.method == 'POST':
        signupForm = UserSignupForm(request.POST)

        if signupForm.is_valid():
            signupForm.save()
            messages.success(request, 'Account created!') 
            return redirect(reverse('blog:home'))

        else:
            signupForm = UserSignupForm()
        return render(request, 'myblog/register.html', {'signupForm': signupForm})

def signupPage(request):
    signupForm = UserSignupForm()
    return render(request, 'myblog/register.html', {'signupForm': signupForm})
