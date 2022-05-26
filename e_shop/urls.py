from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .settings import *
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('', include('eshop_account.urls')),
    path('', include('eshop_products.urls')),
    path('', include('search.urls')),
    path('', include('eshop_contactUs.urls')),
    path('', include('eshop_order.urls')),
    path('', include('eshop_favlist.urls')),
    path('',include("eshop_comment.urls")),
    path('about_us/',about_us)

]
if DEBUG:
    urlpatterns = urlpatterns + static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns = urlpatterns + static(MEDIA_URL, document_root=MEDIA_ROOT)
