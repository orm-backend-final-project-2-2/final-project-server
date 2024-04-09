import json
from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from faker import Faker
from exercises_info.models import ExercisesInfo


class ExercisesInfoTestCase(TestCase):
    """초기설정을 위한 함수"""

    def setUp(self):
        self.fake = Faker()
        self.admin_info = self.create_fake_user_info()

        self.admin = User.objects.create_superuser(**self.admin_info)
        self.user_info = self.create_fake_user_info()
        self.user = User.objects.create_user(**self.user_info)

        self.exercise1_request = self.create_fake_exercise_request()
        self.exercise1 = ExercisesInfo.objects.create(
            author=self.admin, **self.exercise1_request
        )
        self.exercise2_request = self.create_fake_exercise_request()
        self.exercise2 = ExercisesInfo.objects.create(
            author=self.admin, **self.exercise2_request
        )

    def create_fake_user_info(self):
        return {
            "username": self.fake.user_name(),
            "password": self.fake.password(),
        }

    def create_fake_exercise_request(self):
        return {
            "title": self.fake.word(),
            "description": self.fake.text(),
            "video": self.fake.file_name(),
        }

    # 모든 사용자가 운동 정보 리스트를 볼 수 있는지 확인
    def test_all_users_can_view_exercises_list(self):
        response = self.client.get(reverse("exercisesinfo-list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.exercise1.title)
        self.assertContains(response, self.exercise2.title)

    # 모든 사용자가 운동 정보 상세를 볼 수 있는지 확인
    def test_all_users_can_view_exercise_detail(self):
        response = self.client.get(
            reverse("exercisesinfo-detail", args=[self.exercise1.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.exercise1.title)

        response = self.client.get(
            reverse("exercisesinfo-detail", args=[self.exercise2.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.exercise2.title)

    # 관리자만 운동 정보를 생성할 수 있는지 확인
    def test_admin_can_create_exercise(self):
        self.client.login(**self.admin_info)
        response = self.client.post(
            reverse("exercisesinfo-list"),
            data=self.exercise1_request,
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(ExercisesInfo.objects.count(), 3)

    # 일반유저가 운동 정보를 생성할 수 있는지 확인
    def test_user_can_create_exercise(self):
        self.client.login(**self.user_info)
        response = self.client.post(
            reverse("exercisesinfo-list"),
            data=self.exercise1_request,
        )
        self.assertEqual(response.status_code, 403)
        self.assertEqual(ExercisesInfo.objects.count(), 2)

    # 관리자만 운동 정보를 수정할 수 있는지 확인
    def test_admin_can_update_exercise(self):
        self.client.login(**self.admin_info)

        # 데이터 전송 시 Content-Type 설정
        content_type = "application/json"
        data = json.dumps(self.exercise2_request)

        response = self.client.put(
            reverse("exercisesinfo-detail", args=[self.exercise1.id]),
            data=data,
            content_type=content_type,
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            ExercisesInfo.objects.get(id=self.exercise1.id).title,
            self.exercise2.title,
        )

    # 일반유저가 운동 정보를 수정할 수 있는지 확인
    def test_user_can_update_exercise(self):
        self.client.login(**self.user_info)
        response = self.client.put(
            reverse("exercisesinfo-detail", args=[self.exercise1.id]),
            data=self.exercise2_request,
        )
        self.assertEqual(response.status_code, 403)
        self.assertEqual(
            ExercisesInfo.objects.get(id=self.exercise1.id).title,
            self.exercise1.title,
        )

    # 관리자만 운동 정보를 삭제할 수 있는지 확인
    def test_admin_can_delete_exercise(self):
        self.client.login(**self.admin_info)
        response = self.client.delete(
            reverse("exercisesinfo-detail", args=[self.exercise1.id])
        )
        self.assertEqual(response.status_code, 204)
        self.assertEqual(ExercisesInfo.objects.count(), 1)

    # 일반유저가 운동 정보를 삭제할 수 있는지 확인
    def test_user_can_delete_exercise(self):
        self.client.login(**self.user_info)
        response = self.client.delete(
            reverse("exercisesinfo-detail", args=[self.exercise1.id])
        )
        self.assertEqual(response.status_code, 403)
        self.assertEqual(ExercisesInfo.objects.count(), 2)
