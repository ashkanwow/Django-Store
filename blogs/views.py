from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Content

def index(request):
    blogs = Content.objects.order_by('-submite_date').filter(is_published=True)
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)

    context = {
        'blogs' : paged_blogs
    }
    return render(request,'blogs/blogs.html',context)


def blogcontent(request, blogcontent_id):
    blogcontent = get_object_or_404(Content, pk=blogcontent_id)
    context = {
        'blogcontent' : blogcontent
    }
    return render(request, 'blogs/blogcontent.html', context)
