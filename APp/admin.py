from django.contrib import admin
from .models import Registration
# Register your models here.
class RegiAdmin(admin.ModelAdmin):
    list_display=['name','password','email','cno','reg_id']
admin.site.register(Registration,RegiAdmin)