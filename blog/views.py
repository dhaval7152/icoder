from blog.models import Post
from django.shortcuts import render, HttpResponse

# Create your views here.
def blogHome(request): 
    allposts=Post.objects.all()
    print(allposts)
    context={'allposts':allposts}
    return render(request,'blog/blogHome.html',context)

def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug)[0]
    print(post)
    context={'post':post}
    return render(request,'blog/blogPost.html',context)
