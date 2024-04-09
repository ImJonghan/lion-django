from django.contrib import admin
from blog.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'modify_dt', 'create_dt', 'slug')
    list_filter=("modify_dt",)
    search_fields=('title', 'content')
    prepopulated_fields = {"slug":("title", )}
    
    # 추가
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')
    def tag_list(self, obj):
        return ', '.join(o.name for o in obj.tags.all())