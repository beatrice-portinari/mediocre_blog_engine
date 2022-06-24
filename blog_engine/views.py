
from .models import Post, Comment
from .forms import CommentForm
from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseRedirect


class BlogListView(ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 10

class BlogDetailView(DetailView):
    model = Post
    template_name = 'details.html'
    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, pk):
       post = get_object_or_404(Post, pk=pk)
       form = CommentForm(request.POST)

       if form.is_valid():
           obj  = form.save(commit=False)
           obj.post = post
           obj.author = self.request.user
           obj.save()
           return HttpResponseRedirect(request.path_info)