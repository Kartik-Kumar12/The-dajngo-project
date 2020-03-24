from django.contrib import admin
from .models import Item,Order

# Register your models here

# Adding features to itemList admin page

class Itemlistings(admin.ModelAdmin):

   list_display = ('id','desc','price')
   list_display_links =('id','desc')
   list_per_page =30
   search_fields=('desc','status','price')
   list_filter=('status',)


# Adding features to orderList admin page
class Orderlistings(admin.ModelAdmin):

    list_display = ('id','index','order_date','user')
    list_display_links = ('id','index')
    list_per_page =30
    search_fields=('index','user','state','city','zipcode')
    list_filter=('user',)

admin.site.register(Item,Itemlistings)
admin.site.register(Order,Orderlistings)