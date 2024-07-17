from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_stores),
    path('<int:id>', views.search_upt_delete)
]

