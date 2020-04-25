from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


app_name = 'contacts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contact_id>/', views.detail, name='detail'),
    path('<int:contact_id>/edit', views.contact_edit_view, name='edit'),
    path('create', views.contact_create_view, name='create'),
    path('<int:contact_id>/postcard', views.postcard_view, name='create')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
