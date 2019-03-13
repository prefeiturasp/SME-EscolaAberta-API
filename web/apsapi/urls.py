"""apsapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include
from rest_framework import routers


#-----------------arquivos staticos-------------------------------------------------
from django.conf import settings
from django.conf.urls.static import static
#-----------------------------------------------------------------------------------


from core.api.viewsets import NucleoViewSet
from debitos.api.viewsets import DebitosViewSet
from creditos.api.viewsets import CreditosViewSet
from testimagem.api.viewsets import MinhasImagensViewSet


router = routers.DefaultRouter()
router.register(r'api/billingCycles', NucleoViewSet,base_name='Nucleo')
router.register(r'api/debitos', DebitosViewSet)
router.register(r'api/creditos', CreditosViewSet)
router.register(r'api/album', MinhasImagensViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)