from django.urls import path,include
from . import views
# from . import mqttViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('', views.home, name='home'),
   path('cadastroPesquisa/', views.cadastroPesquisa, name='cadastroPesquisa'),
   path('formulario/', views.formulario, name='formulario'),
   path('base/', views.Base, name='Base'),
   path('Footer/', views.Footer, name='Footer'),
   path('login/', views.Footer, name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)