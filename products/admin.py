from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import *
from mapwidgets.widgets import GooglePointFieldInlineWidget
from django.contrib.gis.db.models import PointField
# from .models import Product, TargetMarket,Vendor,Catergory,Brand,TargetMarketCategory
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','unit_price','shop_categorie','brand')
    list_filter = ('shop_categorie','visibility')

class TargetMarketAdmin(admin.ModelAdmin):
    list_display = ('name','target_categorie')
    

class TargetMarketCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','description')


class VendorAdmin(admin.ModelAdmin):
    formfield_overrides = {
        PointField: {"widget": GooglePointFieldInlineWidget}
    }
    list_display = ('business','nameTrading','phoneSales','emailSales','mainAddressCity')
    list_filter = ('business','mainAddressCity')

class CatergoryAdmin(admin.ModelAdmin):
   
    # fieldsets = [
    #     (None, {'fields': ['reference','qrCode','picture','location','deliveryAddress','unitNumber','package_user','available','valid']}),
    # ]
    list_display = ('name','time_update','description')
    list_filter = ('name','time_update')

class BrandAdmin(admin.ModelAdmin):
   
    # fieldsets = [
    #     (None, {'fields': ['reference','qrCode','picture','location','deliveryAddress','unitNumber','package_user','available','valid']}),
    # ]
    list_display = ('name','vendor_id','time_update')
    list_filter = ('targetMarket','time_update')

    
admin.site.register(Product,ProductAdmin)
admin.site.register(TargetMarket,TargetMarketAdmin)
admin.site.register(TargetMarketCategory,TargetMarketCategoryAdmin)
admin.site.register(Vendor,VendorAdmin)
admin.site.register(Catergory,CatergoryAdmin)
admin.site.register(Brand,BrandAdmin)