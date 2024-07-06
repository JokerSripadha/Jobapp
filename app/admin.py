from django.contrib import admin
from app.models import *
# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display=('__str__','title','date','salary')
    list_filter=('date','salary','expiry')
    search_fields=('title','salary','description')
    fieldsets=(
         ('Basic Information',{
            'fields':('title','description')
        }),
         ('Additional Information',{
             'classes':('collapse','wide'),
             'fields':(('expiry','salary'),'slug','location')
         }
             
         ),
    )


admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)
