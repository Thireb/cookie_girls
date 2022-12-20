from django.urls import path

from . import views

""" 
    urls for index, detail, new-form, and update.
    
"""
urlpatterns = [
    
    
    
    path('',views.index, name='index'),
    path('post/<int:pk>/',views.detail,name='detail'),
    path('form/',views.new_post,name='new-form'),

    #ajax url for update
    path('update',views.updatePost, name='update'),
    
    #feedback against a post
    path('post/<int:pk>/feedback',views.feedback_against_post, name='feedback_post'),
    #Feedback Success
    path('success/',views.Success.as_view(),name='success'),
    #Delete View
    path('delete',views.deletePost,name='delete'),
    
    
]
