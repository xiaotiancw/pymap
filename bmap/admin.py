from django.contrib import admin

from .models import HotelAccInfo
# Register your models here.

#admin.site.register(HotelAccInfo)

class HotelAccInfoAdmin(admin.ModelAdmin):
    list_display = ("name", "gender", "idcard", "birth",
                    "city", "hotel", "room", "checkintime", "checkouttime")
    list_filter = ("name", "city", "hotel")

admin.site.register(HotelAccInfo, HotelAccInfoAdmin)