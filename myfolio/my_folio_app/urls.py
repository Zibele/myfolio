from django.urls import path
from . import views

app_name = 'my_folio_app'

urlpatterns = [
    path('', views.index_page, name ='index_page'),
]
