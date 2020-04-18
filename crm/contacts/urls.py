from django.urls import path

from . import views

app_name = 'contacts'
urlpatterns = [
    # ex: /contacts/
    path('', views.index, name='index'),
    # ex: /contacts/5/
    path('<int:contact_id>/', views.detail, name='detail'),
]
