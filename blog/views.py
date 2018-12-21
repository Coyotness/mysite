from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator
from blog.models import Blog, BlogType

def blog_list(request):
    # 分页器
    blogs_all_list = Blog.objects.all()
    pagintor = Paginator(blogs_all_list, 10)  # 每10页进行分页
    page_num = request.GET.get('page', 1)  # get请求获取url的页面参数
    page_of_blogs = pagintor.get_page(page_num)

    context = {}
    context['page_of_blogs'] = page_of_blogs
    context['blog_types'] = BlogType.objects.all()
    return render_to_response('blog/blog_list.html', context)

def blog_detail(request, blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog, pk=blog_pk)
    return render_to_response('blog/blog_detail.html', context)

def blogs_with_type(request, blogs_with_type):
    context = {}
    blog_type = get_object_or_404(BlogType, pk=blogs_with_type)
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)  #传入变量并筛filter选
    context['blog_type'] = blog_type
    return render_to_response('blog/blogs_with_type.html', context)
