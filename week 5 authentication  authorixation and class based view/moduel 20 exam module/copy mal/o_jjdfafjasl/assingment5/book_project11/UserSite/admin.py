from django.contrib import admin
from . models import CategoryModel, PostModel,Userprofile,Borrow_History
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category',)}
    list_display =['category', 'slug']
    
admin.site.register(CategoryModel,CategoryAdmin)
admin.site.register(PostModel)
admin.site.register(Userprofile)
admin.site.register(Borrow_History)
