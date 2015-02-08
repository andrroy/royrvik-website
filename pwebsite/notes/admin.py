from django.contrib import admin
from notes.models import Post, Category


class PostAdmin(admin.ModelAdmin):
	list_display = ('title','submit_date','commited_by',)


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)
	fields = ('name',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

from vb.models import Server, Operatingsystem, Nat_rules

class VirtualboxServerAdmin(admin.ModelAdmin):
	list_display = ('title',)

class OperatingSystemAdmin(admin.ModelAdmin):
	list_display = ('name','imagepath',)

class NatRulesAdmin(admin.ModelAdmin):
	list_display = ('name',)

admin.site.register(Server, VirtualboxServerAdmin)
admin.site.register(Operatingsystem, OperatingSystemAdmin)
admin.site.register(Nat_rules, NatRulesAdmin)
