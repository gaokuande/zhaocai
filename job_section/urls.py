from django.urls import path
from .views import job_post, job_find, job_search, job_submit

urlpatterns = [
    path('post', job_post, name='job-post'),
    path('find', job_find, name='job-find'),
    path('search', job_search, name='job_search'),
    path('submit', job_submit, name='job_submit'),
]
