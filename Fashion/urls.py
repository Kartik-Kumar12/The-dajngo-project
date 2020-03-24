
from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.home,name='home'),
    path('log_in',views.log_in,name='log_in'),
    path('sign_in',views.sign_in,name='sign_in'),
    path('log_out',views.log_out,name='log_out'),
    path('order/<int:pk>',views.order,name='order'),
    path('my_orders',views.my_orders,name='my_orders'),
    path('contact_us',views.contact,name="contact"),
    
]
