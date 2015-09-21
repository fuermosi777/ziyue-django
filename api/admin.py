from django.contrib import admin
from api.models import *

class PostAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_filter = ('vendor',)

admin.site.register(Category)
admin.site.register(Vendor)
admin.site.register(Post, PostAdmin)
admin.site.register(Post_image)
