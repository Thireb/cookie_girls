from django.urls import path

from . import views

""" 
    urls for index, detail, new-form, and update.
    
"""
urlpatterns = [
    
    
    
    path('',views.Index.as_view(), name='index'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='detail'),
    path('form/',views.Newpost.as_view(),name='new-form'),

    #ajax url for update
    path('update',views.Updatepost.as_view(), name='update'),
    
    #feedback against a post
    path('post/<int:pk>/feedback',views.Feedback.as_view(), name='feedback_post'),
    #Feedback Success
    path('success/',views.Success.as_view(),name='success'),
    #Delete View
    path('delete',views.Deletepost.as_view(),name='delete'),
    
    
]
