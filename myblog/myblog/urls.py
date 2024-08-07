"""
URL configuration for myblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from blog.views import *

urlpatterns = [
    path('',home,name="home"),
    path('admin/', admin.site.urls),
    path('login/',login_view,name='login'),
    path('profile/',profile,name='profile'),
    path('signup/',register,name='register'),
    path('create_post/',create_post,name='create_post'),
    path('post/',page,name='post'),
    path('logout/',logout_view,name='logout'),
    path('post/<int:id>/', post_detail, name='post_detail'),
    path('delete_post/<int:id>',delete_post,name='delete_post'),
    path('post/update/<int:id>',update_post,name='update_post')
]


from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                    document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()  