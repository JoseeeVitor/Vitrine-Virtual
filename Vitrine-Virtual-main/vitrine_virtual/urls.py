from django.contrib import admin           #acessando o admin
from django.urls import path, include      #incluindo urls de outros apps
from django.conf import settings           #importando as configurações do projeto
from django.conf.urls.static import static #importando para servir arquivos estáticos


urlpatterns = [path('admin/', admin.site.urls),
               path('', include('core.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)