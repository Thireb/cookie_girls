from django.contrib import admin

from .models import FeedbackPost, Post

# Register your models here.

@admin.register(FeedbackPost)
class FeedbackPostAdmin(admin.ModelAdmin):
    '''Admin View for FeedbackPost'''

    list_display = ('name','post','email',)
    list_filter = ('email','post',)
    search_fields = ('name','email',)
    ordering = ('post',)




@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = ('name','title','created_at',)
    list_filter = ('created_at','published_at','name',)
    search_fields = ('title','name',)
    ordering = ('created_at',)
