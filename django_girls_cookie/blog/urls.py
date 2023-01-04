from django.urls import path

from . import views

""" 
    urls for index, detail, new-form, and update.
    
"""
urlpatterns = [
    
    
    
    path('',views.PostListView.as_view(), name='index'),
    #path('update/<int:pk>/',views.UpdatePost.as_view(), name='update-post'),
    
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='detail'),
    path('form/',views.NewPostCreateView.as_view(),name='new-form'),

    #ajax url for update
    path('update/<int:pk>/',views.UpdatePost.as_view(), name='update'),
    
    #feedback against a post
    path('post/<int:pk>/feedback',views.FeedbackOfPostView.as_view(), name='feedback_post'),
    #Feedback Success
    path('success/',views.SuccessView.as_view(),name='success'),
    #Delete View
    path('delete/<int:pk>/',views.Deletepost.as_view(),name='delete'),
    
    
]
