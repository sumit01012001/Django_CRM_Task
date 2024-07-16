from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),  


]
