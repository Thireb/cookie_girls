from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import TemplateView

from .forms import FeedbackPostForm, PostForm
from .models import Post

# Create your views here.


# url route = index
def index(request):
    posts = Post.objects.filter(published_at__lte=datetime.now()).order_by('-published_at')
    return render(request,'blog/index.html',{'posts': posts})


class Success(TemplateView):
    template_name = "blog/success.html"

# url route = detail
def detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'blog/detail.html',{'post':post})


#url route = new-form
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.name = request.user
            post.published_at = timezone.now()
            post.save()
            return redirect('detail',pk=post.pk)
    else:
        form = PostForm()
    return render(request,'blog/new_form.html',{'form':form})

#route at 'update'
#Update using ajax in the detail page
def updatePost(request):
    if request.method == 'POST':
        try:
            post_id = request.POST.get('post_to_update')
            title = request.POST.get('title')
            text = request.POST.get('text')
            post = get_object_or_404(Post,pk = post_id)
            post.title = title
            post.text = text
            post.publish()
            post.save()
            return JsonResponse({'Updated':True}, status = 200)
        except:
            return JsonResponse({'Updated':False}, status = 400)
    else:
        return JsonResponse({'Updated':False}, status = 400)
        
        

#New feedback post form
def feedback_against_post(request, pk):
    post_to_be_saved_against = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        feedPostForm = FeedbackPostForm(request.POST  )
        if feedPostForm.is_valid():
            feed = feedPostForm.save(commit=False)
            feed.name = request.user
            feed.post = post_to_be_saved_against
            feed.save()
            return redirect(reverse_lazy('success'))
    else:
        feedPostForm = FeedbackPostForm()
    return render(request,'blog/feedback.html',{'form':feedPostForm})


#Delete view, pass the id to delete it.
def deletePost(request):
    try:

        pkey = request.GET.get('post_to_delete')
        post = get_object_or_404(Post, pk=pkey)
        post.delete()
        return JsonResponse({'Deleted':True}, status = 200)
    except:
        return JsonResponse({"Deleted":False}, status=400)