from django.contrib import admin
from .models import *


class BlogAdmin(admin.ModelAdmin):
    list_display = ('activity_name', 'starttime', 'endtime')

admin.site.register(Activity, BlogAdmin)



class OrgAdmin(admin.ModelAdmin):
    list_display = ('org_name', 'authorized', 'slug')

admin.site.register(Organization, OrgAdmin)