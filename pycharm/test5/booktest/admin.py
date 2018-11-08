from django.contrib import admin
from .models import *


class AreaStackedInline(admin.TabularInline):
    model = HeroInfo  # 关联子对象
    extra = 4  # 额外编辑2个子对象


@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date']
    list_per_page = 10  # 每页显示多少个
    actions_on_top = True  # 动作显示在哪
    actions_on_bottom = True
    # fields = ['btitle']  # 编辑页字段

    fieldsets = (
        ('基本', {'fields': ['btitle']}),
        ('高级', {'fields': ['bpub_date']})
    )

    # 关联对象
    inlines = [AreaStackedInline]


# Register your models here.
# admin.site.register(BookInfo, BookInfoAdmin)
@admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender', 'hbook']
    search_fields = ['hname']  # 搜索

    fieldsets = (
        ('基本', {'fields': ['hname']}),
        ('高级', {'fields': ['hbook']})
    )


# admin.site.register(HeroInfo)
admin.site.register(PicTest)

# 注册商品类
admin.site.register(GoodsInfo)

admin.site.register(Blog)
