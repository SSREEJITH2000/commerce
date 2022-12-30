from django.contrib import admin
from . models import category,product
# Register your models here.
class admin_category(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,admin_category)

class admin_product(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(product,admin_product)
