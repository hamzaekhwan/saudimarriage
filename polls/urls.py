

from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path


urlpatterns = [
    path('contract',views.contract , name='contract'),
    path('makeContract',views.makeContract , name='makeContract'),
    path('makeDate',views.makeDate , name='makeDate'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


