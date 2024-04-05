from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView
# Create your views here.

class PostLV(ListView):
    model = Post
    template_name = "blog/post_all.html" 
    context_object_name = 'posts' 
    paginate_by = 1

class PostDV(DetailView):
    model=Post
    template_name="blog/post_detail.html"

#--- ArchiveView
class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'
    template_name = "blog/post_archive.html"


class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True
    template_name = "blog/post_archive_year.html"



class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'
    template_name = "blog/post_archive_month.html"



class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'
    template_name = "blog/post_archive_day.html"



class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'
    template_name = "blog/post_archive_day.html"
