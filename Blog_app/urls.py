from django.urls import path
from .views import Blog_View,Blog_detail,add_blog,edit_blog,delete_blog

urlpatterns = [
    path('',Blog_View,name='home'),
    path('blog_detail/<int:id>',Blog_detail,name='blog_detail'),
    path('add_Blog/',add_blog,name='add_blog'),
    path('blog_edit/<int:id>',edit_blog,name='blog_edit'),
    path('blog_delete/<int:id>',delete_blog,name='blog_delete'),
]