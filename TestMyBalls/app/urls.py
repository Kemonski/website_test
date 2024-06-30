from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home_page, name='HOMEPAGE'),
    path ('thankyou/', views.thankyou, name='THANKPAGE'),
    path ('usagis/', views.bunny_page, name='USAGIPAGE'),
    path('profiles/<int:pk>/', views.profile_detail, name='profile_detail'),
    path('payment/', views.payment_page, name='payment_success'),
    path ('LoRe/', views.login, name='login'),
    path ('crud/', views.crud_html, name='BUNNYPAGE'),
    path('bunny/new/', views.usagiinfo_create, name='usagiinfo_create'),
    path('bunny/<int:pk>/edit/', views.usagiinfo_update, name='usagiinfo_update'),
    path('bunny/<int:pk>/delete/', views.usagiinfo_delete, name='usagiinfo_delete'),
]