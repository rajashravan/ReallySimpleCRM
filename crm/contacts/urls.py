from django.urls import path

from . import views

app_name = 'contacts'
urlpatterns = [
    # ex: /contacts/
    path('', views.index, name='index'),
    # ex: /contacts/5/
    path('<int:contact_id>/', views.detail, name='detail'),
    path('<int:contact_id>/edit', views.contact_edit_view, name='edit'),
    path('create', views.contact_create_view, name='create')
]
