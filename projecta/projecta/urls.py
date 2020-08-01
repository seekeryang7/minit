"""projecta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from board import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
    path('network', views.network, name='network'),
    
    path('board/',views.board, name='board'),
    path('board/notice',views.notice, name='notice'),
    path('board/qa',views.qa,name='qa'),

    path('board/detail_general/<int:pk_selected>',views.detail_general, name='detail_general'),
    path('board/detail_notice/<int:pk_selected>',views.detail_notice, name='detail_notice'),
    path('board/detail_qa/<int:pk_selected>',views.detail_qa, name='detail_qa'),
    path('board/write_general',views.write_general, name='write_general'),
    path('board/write_notice',views.write_notice, name='write_notice'),
    path('board/write_qa',views.write_qa, name='write_qa'),

    path('contact/',views.contact, name='contact'),

    path('curriculum', views.curriculum, name='curriculum'),
    path('about', views.about, name='about'),


]
