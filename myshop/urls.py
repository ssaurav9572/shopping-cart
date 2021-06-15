"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
urlpatterns = [
path('admin/', admin.site.urls),
path('cart/', include('cart.urls', namespace='cart')),
path('', include('shop.urls', namespace='shop')),
]
urlpatterns = [
    path('admin/', admin.site.urls),
]
from django.urls import path
from . import views
app_name = 'shop'
urlpatterns = [
path('', views.product_list, name='product_list'),
path('<slug:category_slug>/', views.product_list,
name='product_list_by_category'),
path('<int:id>/<slug:slug>/', views.product_detail,
name='product_detail'),]
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
path('admin/', admin.site.urls),
path('', include('shop.urls', namespace='shop')),
]
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
# ...
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

