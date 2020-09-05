from django.contrib import admin
from recruiter.models import hydjobinfo,mumbaijobinfo,delhijobinfo

# Register your models here.
class hydjobadmin(admin.ModelAdmin):
    list_display=['date','cname','title','phonenum']

class delhijobadmin(admin.ModelAdmin):
    list_display=['date','cname','title','phonenum']

class mumbaijobadmin(admin.ModelAdmin):
    list_display=['date','cname','title','phonenum']

admin.site.register(hydjobinfo,hydjobadmin)
admin.site.register(delhijobinfo,delhijobadmin)
admin.site.register(mumbaijobinfo,mumbaijobadmin)
