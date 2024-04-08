from django.db import models
from django.contrib.auth.models import User


class ExercisesInfo(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="exercises_info"
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    video = models.ImageField(upload_to="exercises_info_video/", blank=True)

    def __str__(self):
        return f"{self.title}"


class FocusArea(models.Model):
    exercise = models.ForeignKey(
        ExercisesInfo, on_delete=models.CASCADE, related_name="focus_areas"
    )
    focus_area = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.focus_area}"


class ExercisesAttribute(models.Model):
    exercise = models.ForeignKey(
        ExercisesInfo, on_delete=models.CASCADE, related_name="exercise_attributes"
    )
    need_set = models.BooleanField(default=False)
    need_rep = models.BooleanField(default=False)
    need_weight = models.BooleanField(default=False)
    need_duration = models.BooleanField(default=False)
    need_speed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.attribute}"
