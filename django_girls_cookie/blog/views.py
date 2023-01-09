
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
    DeleteView,
    CreateView,
    UpdateView,
)
from .forms import FeedbackPostForm, PostForm
from .models import Post

# Create your views here.


# url route = index
# Home of the site, displays all posts in latest at top order.
class PostListView(ListView):
    template_name = "blog/index.html"
    context_object_name = "posts"
    queryset = Post.objects.order_by("-published_at")


# Success template, used after feedback submitted form.
class SuccessView(TemplateView):
    template_name = "blog/success.html"


# Post Detail View, to display each post in detail, comes after PostListView
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"
    context_object_name = "post"


# New Post, to save a new post with taking current Admin user i.e. Ahmad
class NewPostCreateView(CreateView):
    template_name = "blog/new_form.html"
    form_class = PostForm
    model = Post

    def form_valid(self, form):
        post = form.save(commit=False)
        post.name = self.request.user
        post.save()
        return redirect("detail", pk=post.pk)


class UpdatePost(UpdateView):
    model = Post
    context_object_name = "post"
    fields = [
        "title",
        "text",
    ]
    success_url = reverse_lazy("index")


class FeedbackOfPostView(CreateView):
    form_class = FeedbackPostForm
    template_name = "blog/feedback.html"
    def form_valid(self, form):

        post = get_object_or_404(Post, pk=self.kwargs["pk"])
        feed = form.save(commit=False)
        feed.name = self.request.user
        feed.post = post
        feed.save()
        return redirect(reverse_lazy("success"))


class deletePostView(DeleteView):
    model = Post
    success_url = reverse_lazy("index")
    
