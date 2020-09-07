from basic_app import views
from django.urls import path

app_name = 'basic_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('frontend/', views.FrontEndView.as_view(), name='frontend'),
    path('backend/', views.BackEndView.as_view(), name='backend'),
]
