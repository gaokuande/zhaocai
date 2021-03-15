from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post


def job_post(request):
    return render(request, 'job-section/job-post.html')


def job_find(request):
    return render(request, 'job-section/find-job.html')

def job_search(request):
    q = request.GET.get('q')
    post_list = Post.objects.filter(title__icontains=q)
    pag = Paginator(post_list, 10)
    page = request.POST.get('page')
    page = pag.get_page(page)
    return render(request, 'job-section/find-job.html', {'post_list': post_list})

def job_submit(request):
    if request.method == "POST":
        title = request.POST.get('title')
        company = request.POST.get('company')
        salary = request.POST.get('salary')
        address = request.POST.get('address')
        detail = request.POST.get('detail')
        
        sub = Post()
        sub.title = title
        sub.company = company
        sub.salary = salary
        sub.address = address
        sub.detail = detail
        sub.save()
    return render(request, 'job-section/find-job.html')