from django.urls import path
from .apps import APP_NAME
from . import views
app_name=APP_NAME
urlpatterns = [
    path('',views.IndexView().home,name='home'),
    path('search/',views.IndexView().search,name='search'),
    path('logout/',views.IndexView().search,name='logout'),
    path('login/',views.IndexView().search,name='login'),
    path('about/',views.IndexView().search,name='about'),
    path('terms/',views.IndexView().search,name='terms'),
]
