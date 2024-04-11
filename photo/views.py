from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Album, Photo
# Create your views here.

class AlbumLV(ListView):
    model=Album
    # context_object_name = 'object_list'
    # template_name='photo/album_list.html'    
    # ListView의 기본 템플릿 : 앱이름/모델_list.html
    # context = {'object_list':....}
    # def get_queryset(self) -> QuerySet[Any]:        
    #     return self.model.objects.all()    
    # def get_object # DV
    # def get_context_data

class AlbumDV(DetailView):
    model=Album
    template_name='photo/album_detail.html'
    # pk를 통해서 특정 앨범만 가져온다

class PhotoDV(DetailView):
    model=Photo
    template_name='photo/photo_detail.html'
class Question:pass
class Choice:pass