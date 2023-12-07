from django.contrib import admin

from .models import Post, Comment, Category

class PostAdmin(admin.ModelAdmin):
  list_display = ("Title", "Category", "Date_Published",)

admin.site.register(Post,PostAdmin)
class CommentAdmin(admin.ModelAdmin):
  list_display = ("Post_ID", "User_ID", "Date_Posted",)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Category)
