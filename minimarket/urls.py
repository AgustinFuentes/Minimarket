from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('ver_carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('agregar-al-carrito/<int:producto_id>', views.agregar_al_carrito, name='agregar-al-carrito'),
    path('eliminar-producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)