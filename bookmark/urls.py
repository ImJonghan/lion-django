# polls 폴더에 urls.py가 업어서 새로 생성

from django.urls import path

from . import views

app_name = "bookmark"

urlpatterns = [
    path("", views.BookmarkLV.as_view(), name="index"),
    path("<int:pk>/", views.BookmarkDV.as_view(), name="detail"),    
]