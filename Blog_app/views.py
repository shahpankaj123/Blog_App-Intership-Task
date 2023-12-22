from django.shortcuts import render,redirect
from .models import Blog,Category
from .forms import BlogForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.cache import cache


@login_required(login_url='Login')
def Blog_View(request):
    if cache.get('blogs'):
      blogs=cache.get('blogs')
      print('Redis Db')
    else:
        blogs=Blog.objects.select_related()
        cache.set('blogs',blogs,timeout=10)  
    return render(request,'home.html',{'data':blogs})


@login_required(login_url='Login')
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            category= form.cleaned_data['category']
            desc=form.cleaned_data['desc']
            img=form.cleaned_data['img']
            user=request.user
            Blog.objects.create(name=name,user=user,category=category,desc=desc,img=img)
            messages.success(request,"Blog added successfully")
            return redirect('home')
    else:
        form = BlogForm()

    return render(request, 'add_blog.html', {'form': form})


@login_required(login_url='Login')
def Blog_detail(request,id):
    if cache.get('blog'):
      blog=cache.get('blog')
      print('Redis Db')
    else:
        blog=Blog.objects.get(id=id)
        cache.set('blog',blog,timeout=10) 
    return render(request,'Blog_detail.html',{'data':blog})

@login_required(login_url='Login')
def edit_blog(request,id):
  blog=Blog.objects.get(id=id)
  if blog.user==request.user:
    category=Category.objects.all()
    if request.method == 'POST':
          name=request.POST['name']
          category1=request.POST['category']
          blog_desc=request.POST['desc']
          if request.FILES.get('img'):
               img=request.FILES.get('img')
               blog.img=img
          category_obj=Category.objects.get(name=category1)
          blog.name=name
          blog.category=category_obj
          blog.desc=blog_desc
          blog.save()
          messages.success(request,"Blog Updated successfully")
          return redirect('home')
    else:
        return render(request, 'edit_blog.html', {'data':blog,'cat':category})
  else:
     messages.success(request,"You are not authorized to Edit blog")
     return redirect('home')

@login_required(login_url='Login')
def delete_blog(request,id):
    blog_obj=Blog.objects.get(id=id)
    if blog_obj.user==request.user:
       blog_obj.delete()
       messages.success(request,"Blog deleted successfully")
       return redirect('home')
    else:
     messages.success(request,"You are not authorized to Delete blog")
     return redirect('home')
