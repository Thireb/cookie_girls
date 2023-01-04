from datetime import datetime
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.urls import reverse
from django.utils import timezone
from django.views.generic import TemplateView, DetailView, ListView, DeleteView, CreateView, UpdateView
from django.views.generic.edit import FormView
from django.views import View
from .forms import FeedbackPostForm, PostForm
from .models import Post
from django.http import HttpResponse
# Create your views here.


# url route = index
#Home of the site, displays all posts in latest at top order.
class PostListView(ListView):
    template_name = "blog/index.html"
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-published_at')
   
    

#Success template, used after feedback submitted form.
class SuccessView(TemplateView):
    template_name = "blog/success.html"


#Post Detail View, to display each post in detail, comes after PostListView
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"
    context_object_name = 'post'

#New Post, to save a new post with taking current Admin user i.e. Ahmad
class NewPostCreateView(CreateView):
    template_name = 'blog/new_form.html'
    form_class = PostForm
    model = Post
    def form_valid(self, form):
        post = form.save(commit=False)
        post.name = self.request.user
        #post.published_at = timezone.now()
        post.save()
        return redirect('detail',pk=post.pk)    
    
        
class UpdatePost(UpdateView):
    model = Post
    context_object_name ='post'
    fields = ['title','text',]
    success_url = reverse_lazy('index')

#To update a saved post, data is sent using Ajax, OLD VIEW
# class UpdatePostView(UpdateView):
#     model = Post
#     def post(self, request):
        
#         try:
#             post_id = request.POST.get('post_to_update')
#             title = request.POST.get('title')
#             text = request.POST.get('text')
#             post = get_object_or_404(Post,pk = post_id)
            
#         except:
#             return JsonResponse({'Updated':False}, status = 400)
#         post.title = title
#         post.text = text
#         #post.publish()
#         post.save()
#         return JsonResponse({'Updated':True}, status = 200)

class FeedbackOfPostView(CreateView):
    form_class = FeedbackPostForm
    template_name = 'blog/feedback.html'
    #success_url = reverse_lazy('success')
    def form_valid(self, form):
        
        post = get_object_or_404(Post, pk = self.kwargs["pk"])
        feed = form.save(commit=False)
        feed.name = self.request.user
        feed.post = post
        feed.save()
        return redirect(reverse_lazy('success'))
        
class Deletepost(DeleteView):
    model = Post
    success_url = reverse_lazy('index')
    # def form_valid(self):
    #     return None