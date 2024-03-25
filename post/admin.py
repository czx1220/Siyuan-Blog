from django.contrib import admin
from .models import *
# Register your models here.




# class MyAdminSite(admin.AdminSite):
#     site_url = "/post"
#     # pass

# admin_site = MyAdminSite(name="admin")
# admin_site.register(Category)
# admin_site.register(Tag)
# admin_site.register(Post)

from django.contrib import admin
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created']  # 显示的字段
    search_fields = ['title']  # 允许搜索的字段

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # 如果是超级用户，返回所有帖子；否则，只返回当前用户的帖子
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        # 在保存模型时设置当前用户为帖子的所有者
        if not obj.user:
            obj.user = request.user
        obj.save()

admin.site.register(Post, PostModelAdmin)


admin.site.register(Category)
admin.site.register(Tag)
# admin.site.register(Post)
