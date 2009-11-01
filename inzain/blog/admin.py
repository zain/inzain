from django.contrib import admin
from inzain.blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "create_date", "completed", "pub_date", "blurb")
    list_filter = ("completed",)
    search_fields = ("title", "text")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)