"""
URL configuration for system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from hotel_booking import views
from hotel_booking.views import register_view, login_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('booking_list_as_admin/', views.booking_list_as_admin,name="booking_list_as_admin"),
    path('', views.main_system,name="main_system"),
    path('booking_as_admin/', views.booking_as_admin,name="booking_as_admin"),
    path('my_booking_as_admin/', views.my_booking_as_admin,name="my_booking_as_admin"),
    path('booking_as_user/', views.booking_as_user,name="booking_as_user"),
    path('regiregister/', register_view,name="regiregister"),
    path('login/', login_view,name="login"),
    path('logout/', LogoutView.as_view(),name="logout"),
]
