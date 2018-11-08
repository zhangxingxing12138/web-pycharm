from django.contrib import admin
from .models import *


# Register your models here.

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date']


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'hcomment', 'hbook', 'gender']


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
