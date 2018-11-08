from django.contrib import admin
# Register your models here.
from .models import *


class PostAdmin(admin.ModelAdmin):
    class Media:
        js = (
            'js/editor/kindeditor-all.js',
            'js/editor/config.js',
        )


admin.site.register(Banner)

admin.site.register(Post, PostAdmin)

admin.site.register(Category)

admin.site.register(Tags)

admin.site.register(Comment)

admin.site.register(Link)
