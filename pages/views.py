from django.shortcuts import get_object_or_404, render

from pages.models import Lecture, Note, Pset

# Create your views here.


def home(request):
    return render(request, "home.html")


# one
# use lecture context for link
def lecture(request, lecture):
    lecture = get_object_or_404(Lecture, order=lecture)
    psets = Pset.objects.filter(lecture=lecture)
    return render(request, "lectures/detail.html", {"lecture": lecture, "psets": psets})


def note(request, lecture):
    lecture = get_object_or_404(Lecture, order=lecture)
    note = get_object_or_404(Note, lecture=lecture)
    return render(request, "notes/detail.html", {"note": note})


# all
def psets(request, lecture):
    lecture = get_object_or_404(Lecture, order=lecture)
    psets = Pset.objects.filter(lecture=lecture)
    return render(request, "psets/index.html", {"psets": psets})


# one
def pset(request, lecture, slug):
    lecture = get_object_or_404(Lecture, order=lecture)
    pset = get_object_or_404(Pset, lecture=lecture, slug=slug)
    return render(request, "psets/detail.html", {"pset": pset})
