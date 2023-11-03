from django.contrib import admin
from dentry_app.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','country','event','cat','is_active']
    
# Register your models here.
admin.site.register(Product,ProductAdmin)
