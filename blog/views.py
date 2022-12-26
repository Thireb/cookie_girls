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
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["posts"] = Post.objects.filter(published_at__lte=datetime.now()).order_by('-published_at')
    #     return context
    
    

#Success template, used after feedback submitted form.
class SuccessView(TemplateView):
    template_name = "blog/success.html"


#Post Detail View, to display each post in detail, comes after PostListView
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"
    context_object_name = 'post'


#url route = new-form
# def new_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.name = request.user
#             post.published_at = timezone.now()
#             post.save()
#             return redirect('detail',pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request,'blog/new_form.html',{'form':form})


#New Post, to save a new post with taking current Admin user i.e. Ahmad
class NewPostCreateView(CreateView):
    template_name = 'blog/new_form.html'
    form_class = PostForm
    model = Post
    #success_url = reverse_lazy('detail')
    # def post(self, request):
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         post = form.save(commit = False)
    #         post.name = self.request.user
    #         post.published_at = timezone.now()
    #         post.save()
    #         return redirect('detail',pk=post.pk)
    def form_valid(self, form):
        post = form.save(commit=False)
        post.name = self.request.user
        post.published_at = timezone.now()
        post.save()
        return redirect('detail',pk=post.pk)    
    

#route at 'update'
#Update using ajax in the detail page
# def updatePost(request):
#     if request.method == 'POST':
#         try:
#             post_id = request.POST.get('post_to_update')
#             title = request.POST.get('title')
#             text = request.POST.get('text')
#             post = get_object_or_404(Post,pk = post_id)
#             post.title = title
#             post.text = text
#             post.publish()
#             post.save()
#             return JsonResponse({'Updated':True}, status = 200)
#         except:
#             return JsonResponse({'Updated':False}, status = 400)
#     else:
#         return JsonResponse({'Updated':False}, status = 400)
        
        
        
        
# class UpdatePost(UpdateView):
#     #error: quote_from_bytes() expected bytes
#     model = Post
#     context_object_name ='post'
#     fields = ['title','text',]
#     def get_success_url(self):
#         return JsonResponse({'Updated':True}, status = 200)

#To update a saved post, data is sent using Ajax
class UpdatePostView(UpdateView):
    model = Post
    def post(self, request):
        
        try:
            post_id = request.POST.get('post_to_update')
            title = request.POST.get('title')
            text = request.POST.get('text')
            post = get_object_or_404(Post,pk = post_id)
            
        except:
            return JsonResponse({'Updated':False}, status = 400)
        post.title = title
        post.text = text
        post.publish()
        post.save()
        return JsonResponse({'Updated':True}, status = 200)


#New feedback post form
# def feedback_against_post(request, pk):
#     post_to_be_saved_against = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         feedPostForm = FeedbackPostForm(request.POST  )
#         if feedPostForm.is_valid():
#             feed = feedPostForm.save(commit=False)
#             feed.name = request.user
#             feed.post = post_to_be_saved_against
#             feed.save()
#             return redirect(reverse_lazy('success'))
#     else:
#         feedPostForm = FeedbackPostForm()
#     return render(request,'blog/feedback.html',{'form':feedPostForm})

#Feedback against a post, accessible on detail page
class FeedbackOfPostView(CreateView):
    form_class = FeedbackPostForm
    template_name = 'blog/feedback.html'
    #success_url = reverse_lazy('success')
    def form_valid(self, form):
        
        post = get_object_or_404(Post, pk = self.kwargs["pk"])
        feed = form.save(commit=False)
        #feed.name = self.request.user
        feed.post = post
        feed.save()
        return redirect(reverse_lazy('success'))
        
#Delete view, pass the id to delete it.
# def deletePost(request):
#     try:

#         pkey = request.GET.get('post_to_delete')
#         post = get_object_or_404(Post, pk=pkey)
#         post.delete()
#         return JsonResponse({'Deleted':True}, status = 200)
#     except:
#         return JsonResponse({"Deleted":False}, status=400)
    
class Deletepost(DeleteView):
    # def post(self,request):
    #     post = get_object_or_404(Post, pk = request.POST.get("post_to_delete"))
    #     post.delete()
    #     return JsonResponse({'Deleted':True}, status = 200)
    #For future use, currently only GET request is being used for post deletion
    
    def get(self,request):
        post = get_object_or_404(Post, pk = request.GET.get("post_to_delete"))
        post.delete()
        return JsonResponse({'Deleted':True}, status = 200)