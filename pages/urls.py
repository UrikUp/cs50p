from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("weeks/<int:lecture>/", views.lecture, name="week"),
    # many
    path("psets/<int:lecture>/", views.psets, name="psets"),
    # one
    path("psets/<int:lecture>/<slug:slug>/", views.pset, name="pset"),
    path("notes/<int:lecture>/", views.note, name="note"),
    path("sorry/", views.not_ready, name="not_ready"),
]
