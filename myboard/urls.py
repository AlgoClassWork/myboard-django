"""
URL configuration for myboard project.

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
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from ads.views import ad_list, ad_create, ad_delete, ad_edit, register

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    #http://127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),
    #http://127.0.0.1:8000/
    path('', ad_list, name='home' ),
    #http://127.0.0.1:8000/add
    path('add/', ad_create, name='create_ad'),
    #http://127.0.0.1:8000/delete/5
    path('delete/<int:id>/', ad_delete, name='delete_ad'),
    #http://127.0.0.1:8000/edit/10
    path('edit/<int:id>/', ad_edit, name='edit_ad'),
    #http://127.0.0.1:8000/register
    path('register/', register, name='register'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)