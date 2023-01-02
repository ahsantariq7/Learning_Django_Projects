
from django.contrib import admin
from .models import Shop_By_Categories,Shop_By_Brand1,Language,Accessories,Shopping_Bag,Shopping_Bag_Items,slider,Categoryall,Sub_Categoryall,Section,Product,Product_Image,Additional_Information,Color,Shipping_Addres,Payment_Type,Payment_Method
# Register your models here.

class Product_Images1(admin.TabularInline):
    model=Product_Image

class Additional_Informations(admin.TabularInline):
    model=Additional_Information

class Product_Admin(admin.ModelAdmin):
    inlines=[Product_Images1,Additional_Informations]
   
    #list_display: ['name','price','Category','color','section']
    #list_editable: ['Category','section','color']



admin.site.register(Shop_By_Categories)
admin.site.register(Shop_By_Brand1)
admin.site.register(Language)
admin.site.register(Accessories)
admin.site.register(Shopping_Bag)
admin.site.register(Shopping_Bag_Items)
admin.site.register(slider)

admin.site.register(Categoryall)
admin.site.register(Sub_Categoryall)
admin.site.register(Section)
admin.site.register(Product,Product_Admin)
admin.site.register(Product_Image)
admin.site.register(Additional_Information)
admin.site.register(Color)
admin.site.register(Shipping_Addres)
admin.site.register(Payment_Method)
admin.site.register(Payment_Type)


