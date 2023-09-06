from django.contrib import admin
from .models import Goods, Reservation, OrderItem

class OrderItemInline(admin.TabularInline):  
    model = OrderItem
    extra = 1  

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'phone_number', 'user_mail', 'get_goods_name', 'get_total_price']
    inlines = [OrderItemInline]

    def get_goods_name(self, obj):
        return ", ".join([item.goods.name for item in obj.item.all()])
    
    def get_total_price(self, obj):
        return sum([item.goods.price * item.quantity for item in obj.item.all()])

    get_goods_name.short_description = "굿즈 이름"
    get_total_price.short_description = "총 가격"

admin.site.register(OrderItem)  
admin.site.register(Goods)
admin.site.register(Reservation, ReservationAdmin)

