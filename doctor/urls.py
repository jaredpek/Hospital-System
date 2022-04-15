from django.urls import path, re_path
from . import views
from .views import PatientListView, PatientUpdateView, PatientDeleteView
from django.views.static import serve

app_name = 'doctor'

urlpatterns = [
    path('', views.login, name='login'),
    path('homepage/', views.homepage, name='homepage'),
    path('addrecord/', views.addrecord, name='addrecord'),
    path('listpatients/', PatientListView.as_view(), name='listpatients'),
    path('updatepatient/<int:pk>', PatientUpdateView.as_view(), name='updatepatient'),
    path('deletepatient/<int:pk>', PatientDeleteView.as_view(), name='deletepatient'),
]
