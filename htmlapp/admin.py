from django.contrib import admin
from htmlapp.models import DisplayData


# Register your models here.
class User(admin.ModelAdmin):
    list_display=['name','email','age','add']
admin.site.register(DisplayData,User)


