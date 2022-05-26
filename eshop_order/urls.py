from django.urls import path
from .views import *

urlpatterns = [
    path('add-user-order', new_order_creat),
    path('user-order', order_page),
    path('user-order-detail-delete/<detail_id>', order_delete),
    path('request/', send_request),
    path('verify/', verify),

]
