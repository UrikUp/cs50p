from django.db import models


class Lecture(models.Model):
    title = models.CharField(max_length=200)
    youtube = models.URLField(null=True, blank=True)
    topics = models.TextField(null=True)
    order = models.PositiveSmallIntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.order}: {self.title}"


class Note(models.Model):
    lecture = models.OneToOneField(Lecture, on_delete=models.CASCADE, related_name="note")
    # use md for notes
    text = models.TextField(blank=True)

    def __str__(self):
        return f"{self.lecture.order}: {self.lecture.title}"


class Pset(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, related_name="psets")
    order = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)

    # use md
    video = models.TextField(blank=True)
    cite = models.TextField(blank=True)
    description = models.TextField(blank=True)
    hint = models.TextField(blank=True)
    test = models.TextField(blank=True)
    ascii = models.CharField(max_length=50, blank=True)

    # optional. If there is more descriptions
    test_etc = models.TextField(blank=True)
    before_start = models.TextField(blank=True)
    before_end = models.TextField(blank=True)
    demo_start = models.TextField(blank=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["lecture", "order"], name="unique_pset_order_per_lecture")]
        ordering = ["order"]

    def __str__(self):
        return f"{self.lecture.order}-{self.order}: {self.slug}"
