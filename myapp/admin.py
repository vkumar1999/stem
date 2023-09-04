
from django.contrib import admin
from .models import Book
from .models import Post
# from import_export.admin import ExportActionMixin
from import_export.admin import ImportExportMixin

# Register your models here.
class BookAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('title', 'description', 'author', 'year')

class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug', 'status', 'created_on','image')
  list_filter = ('status',)
  search_fields = ['title', 'content']
  
admin.site.register(Post, PostAdmin)

admin.site.register(Book, BookAdmin)
