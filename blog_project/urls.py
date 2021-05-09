
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView, RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/blog/', permanent=True)),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
    path('api/', include('odoo_app.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)