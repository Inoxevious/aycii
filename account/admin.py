from django.contrib import admin
from . models import *
from mapwidgets.widgets import GooglePointFieldInlineWidget
from django.contrib.gis.db.models import PointField
class CountryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        PointField: {"widget": GooglePointFieldInlineWidget}
    }
# Register your models here.
admin.site.register(AccountUser)
admin.site.register(ExecutivesStatment)
admin.site.register(Events)
admin.site.register(Department)
admin.site.register(Executive)
admin.site.register(NoticeBoard)
admin.site.register(Articles)
admin.site.register(UserClass)
admin.site.register(Role)
admin.site.register(Country,CountryAdmin)
admin.site.register(MembershipRole)
admin.site.register(MembershipClass)