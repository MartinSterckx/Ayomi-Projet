from django.urls import path
from . import views





urlpatterns = [
	path('', views.home, name = "home"),
	path("signup/", views.register_user, name="signup"),
	path('informations/', views.informations, name= "informations")
]