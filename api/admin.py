from django.contrib import admin
from api.models import *

class Update_log_admin(admin.ModelAdmin):
	list_display = ('id', 'success', 'vendor', 'counter', 'datetime',)

admin.site.register(Category)
admin.site.register(Vendor)
admin.site.register(Post)
admin.site.register(Post_image)
admin.site.register(Update_log, Update_log_admin)
