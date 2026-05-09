from .models import Lecture


def sidebar_pages(request):
    return {"sidebar_pages": Lecture.objects.all()}
