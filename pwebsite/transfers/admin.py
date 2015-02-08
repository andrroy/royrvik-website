from django.contrib import admin
from transfers.models import SC_Rating, Transfer_Post, RO_Post


class PostAdmin(admin.ModelAdmin):
	list_display = ('poster',)

class RatingAdmin(admin.ModelAdmin):
	list_display = ('post',)

class RoAdmin(admin.ModelAdmin):
	list_display = ('title',)



admin.site.register(Transfer_Post, PostAdmin)
admin.site.register(SC_Rating, RatingAdmin)
admin.site.register(RO_Post, RoAdmin)
