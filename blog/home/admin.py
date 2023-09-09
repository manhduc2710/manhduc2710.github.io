from django.contrib import admin
from .models import Post
# Register your models here.
class ListPost(admin.ModelAdmin):
    list_display = ['ten', 'anh', 'noidung', 'thoigian']
    list_filter = ['thoigian']
admin.site.register(Post, ListPost)