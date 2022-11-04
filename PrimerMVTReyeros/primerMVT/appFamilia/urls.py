from django.urls import path
from appFamilia import views
from appFamilia.views import *

urlpatterns = [
    path("", list_familia),
    path("agregarFamiliar/", addFamiliar),


]