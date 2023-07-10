from django.urls import path
from .import views

app_name = 'admin_crud'

urlpatterns = [
    path('',views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout_view, name='logout_view'),
    path('registrarproduct',views.registrarproduct, name='registrarproduct'),
    path('eliminarproduct/<product_id>',views.eliminarproduct, name='eliminarproduct'),
]