from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


app_name = 'contacts'
urlpatterns = [
    # ex: /contacts/
    path('', views.index, name='index'),
    # ex: /contacts/5/
    path('<int:contact_id>/', views.detail, name='detail'),
    path('<int:contact_id>/edit', views.contact_edit_view, name='edit'),
    path('create', views.contact_create_view, name='create'),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#


# if settings.DEBUG:
#     urlpatterns += urlpatterns('',
#         url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#             'document_root': settings.MEDIA_ROOT,
#         }),
#    )
