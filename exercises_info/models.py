from django.db import models
from account.models import CustomUser as User


class ExercisesInfo(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="exercises_info"
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    video = models.FileField(upload_to="exercises_info_video/", blank=True)
    focus_areas = models.ManyToManyField("FocusArea", related_name="exercise")
    # exercise_attributes = models.OneToOneField(
    #     "ExercisesAttribute", on_delete=models.CASCADE, related_name="exercise"
    # )

    def __str__(self):
        return f"{self.title}"


class FocusArea(models.Model):
    FOCUS_AREA_CHOICES = [
        ("유산소", "유산소"),
        ("가슴", "가슴"),
        ("등", "등"),
        ("어깨", "어깨"),
        ("팔", "팔"),
        ("하체", "하체"),
        ("코어", "코어"),
    ]

    focus_area = models.CharField(max_length=20, choices=FOCUS_AREA_CHOICES)

    def __str__(self):
        return self.get_focus_area_display()


# class ExercisesAttribute(models.Model):
#     need_set = models.BooleanField(default=False)
#     need_rep = models.BooleanField(default=False)
#     need_weight = models.BooleanField(default=False)
#     need_duration = models.BooleanField(default=False)
#     need_speed = models.BooleanField(default=False)
