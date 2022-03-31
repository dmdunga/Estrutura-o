from django.urls import path,include
from . import views
# from . import mqttViews
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('singin', views.singin, name="singin"),
    path('logado', views.logado, name="logado"),
    path('cadsatro', views.Cadastro, name="cadastro"),
 
    path('', include('app1.urls')),



    # path('singin/', views.Footer, name='Footer'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)