from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView
from django.views.generic import TemplateView
from django.conf import settings
# Create your views here.

class PostLV(ListView):
    model = Post
    template_name = "blog/post_all.html" 
    context_object_name = 'posts' 
    paginate_by = 3
    # def get_queryset(self):
    #     return Post.objects.all()

def dummpy_post(request):
    objects = Post.objects.all()
    context = {
        'posts' : objects
    }
    return render(request, "blog/post_all.html", context)

class PostDV(DetailView):
    model=Post
    template_name="blog/post_detail.html"
    # get_queryset - > get_object
    # def get_object(self):pass
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id}-{self.object.slug}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.slug}"
        return context        



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

class TagCloudTV(TemplateView):
    template_name="taggit/taggit_cloud.html"

class TaggedObjectLV(ListView):
    template_name='taggit/taggit_post_list.html'
    model = Post
    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context
    