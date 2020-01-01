from django.contrib import admin
from.models import Product,Registation
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','stock','Description')
admin.site.register(Product,ProductAdmin)

class RegistationAdmin(admin.ModelAdmin):
    list_display = ('Full_name','email','phone_number','password','username')
admin.site.register(Registation,RegistationAdmin)