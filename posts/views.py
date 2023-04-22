from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

@login_required
def home(request):
    posts = Post.objects.all().order_by('-timestamp')
    return render(request, 'posts/home.html', {'posts': posts})

class PostCreateView(CreateView):
    model = Post
    fields = ['content']
    template_name = 'posts/create_post.html'
    success_url = reverse_lazy('posts:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
