"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from crops.models import Crop, Inventory, Harvest
from . import views

# シンプルなホームページのビュー関数
def home_view(request):
    context = {}
    if request.user.is_authenticated:
        context['recent_crops'] = Crop.objects.filter(
            farmer=request.user
        ).order_by('-created_at')[:5]
        
        context['low_stock_items'] = Inventory.objects.filter(
            farmer=request.user,
            quantity__lt=10
        ).order_by('quantity')[:5]
        
        context['recent_harvests'] = Harvest.objects.filter(
            crop__farmer=request.user
        ).order_by('-harvest_date')[:5]
    
    return render(request, 'accounts/index.html', context)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # accountsアプリのURLをインクルード
    path('crops/', include('crops.urls')),  # 追加
    path('', home_view, name='home'),            # ルートURLを設定
    path('delete/inventory/<int:id>/', views.delete_inventory, name='delete_inventory'),
    path('delete/crop/<int:id>/', views.delete_crop, name='delete_crop'),
    path('delete/harvest/<int:id>/', views.delete_harvest, name='delete_harvest'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

