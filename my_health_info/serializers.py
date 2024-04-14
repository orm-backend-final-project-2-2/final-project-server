from rest_framework import serializers
from my_health_info.models import (
    HealthInfo,
    Routine,
    ExerciseInRoutine,
    UsersRoutine,
    MirroredRoutine,
)
from exercises_info.models import ExercisesInfo
from drf_writable_nested import WritableNestedModelSerializer
from exercises_info.serializers import ExercisesInfoSerializer


class HealthInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthInfo
        fields = ["user", "age", "height", "weight", "bmi", "created_at"]
        read_only_fields = ["user", "bmi", "created_at"]


class ExerciseInRoutineSerializer(WritableNestedModelSerializer):
    exercise_info = ExercisesInfoSerializer(source="exercise", read_only=True)
    exercise = serializers.PrimaryKeyRelatedField(
        queryset=ExercisesInfo.objects.all(), write_only=True
    )

    class Meta:
        model = ExerciseInRoutine
        fields = ["routine", "exercise", "order", "exercise_info"]
        read_only_fields = ["routine"]


class RoutineSerializer(WritableNestedModelSerializer):
    username = serializers.SerializerMethodField()
    exercises_in_routine = ExerciseInRoutineSerializer(many=True)

    class Meta:
        model = Routine
        fields = [
            "author",
            "username",
            "title",
            "created_at",
            "is_deleted",
            "like_count",
            "exercises_in_routine",
        ]
        read_only_fields = [
            "author",
            "username",
            "created_at",
            "is_deleted",
            "like_count",
        ]

    def get_username(self, obj):
        return obj.author.username


class MirroredRoutineSerializer(serializers.ModelSerializer):
    exercises_in_routine = ExerciseInRoutineSerializer(many=True)

    class Meta:
        model = MirroredRoutine
        fields = ["title", "author_name", "original_routine", "exercises_in_routine"]
        read_only_fields = [
            "title",
            "author_name",
            "original_routine",
            "exercises_in_routine",
        ]


class UsersRoutineSerializer(serializers.ModelSerializer):
    mirrored_routine = MirroredRoutineSerializer(read_only=True)

    class Meta:
        model = UsersRoutine
        fields = ["user", "routine", "mirrored_routine", "need_update"]
        read_only_fields = ["user", "routine", "need_update"]
