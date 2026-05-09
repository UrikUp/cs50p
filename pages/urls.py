from django.urls import path
from . import views

urlpatterns = [
    path("", views.lectures, name="weeks"),
    path("weeks/<int:lecture>/", views.lecture, name="week"),
    # many
    path("psets/<int:lecture>/", views.psets, name="psets"),
    # one
    path("psets/<int:lecture>/<slug:slug>/", views.pset, name="pset"),
    path("notes/<int:lecture>/", views.note, name="note"),
]
