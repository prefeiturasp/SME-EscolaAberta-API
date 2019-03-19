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
from portal.views.modalidades import ModalidadesPraticadas
from portal.views.total_vagas_mat_serie import VagasMatriculasBySerie
from rest_framework import routers

# -----------------arquivos staticos-------------------------------------------------
from django.conf import settings
from django.conf.urls.static import static
# -----------------------------------------------------------------------------------

from escolas.api.viewsets import EscolasViewSet
from turmas.api.viewsets import TurmasViewSet
from servidores.api.viewsets import ServidoresViewSet
from ambientes.api.viewsets import AmbientesViewSet

router = routers.DefaultRouter()
router.register(r'api/escolas', EscolasViewSet)
router.register(r'api/turmas', TurmasViewSet)
router.register(r'api/servidores', ServidoresViewSet)
router.register(r'api/ambientes', AmbientesViewSet)
# router.register('api/modalidades/<int:codesc>', ModalidadesPraticadas.as_view(), base_name='ModalidadeEnsino')

urlpatterns = [
                  path('', include(router.urls)),
                  path('admin/', admin.site.urls),
                  path('api/modalidades/<slug:codesc>', ModalidadesPraticadas.as_view()),
                  path('api/totvagmatbyserie/<slug:codesc>', VagasMatriculasBySerie.as_view()),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
