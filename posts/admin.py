from django.contrib import admin

from .models import Post, PostFile

class PostFileInlineAdmin(admin.StackedInline):
    model = PostFile
    fields = ('file', )
    extra = 0
    can_delete = False

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'is_active', 'is_public']
    list_filter = ['is_active']
    inlines = [PostFileInlineAdmin]
    

    