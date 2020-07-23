import pytest

from fb_post_auth.dtos.fb_post import UserDTO
from fb_post_auth.models.user import User
from fb_post_auth.storages.storage_implementation import StorageImplementation


class TestStorageImplementation:

    @pytest.mark.django_db
    def test_get_user_details_dto_given_user_ids_then_return_user_dtos(
            self, get_user_dtos):
        expected_user_dtos = get_user_dtos
        user_ids = [1, 2, 3, 4]
        storage = StorageImplementation()

        actual_user_dtos = storage.get_user_details_dtos(user_ids=user_ids)

        assert actual_user_dtos == expected_user_dtos

    @pytest.fixture
    def get_user_dtos(self):
        users = [
            {
                'username': 'user1',
                "name": "lakshmi",
                "profile_pic_url": "profile_pic1"
            },
            {
                'username': 'user2',
                "name": "lakshmi",
                "profile_pic_url": "profile_pic2"
            },
            {
                'username': 'user3',
                "name": "lakshmi",
                "profile_pic_url": "profile_pic3"
            },
            {
                'username': 'user4',
                "name": "lakshmi",
                "profile_pic_url": "profile_pic4"
            }
        ]

        for user in users:
            User.objects.create(
                username=user['username'],
                name=user['name'],
                profile_pic_url=user['profile_pic_url'])

        user_ids = [1, 2, 3, 4]
        users = User.objects.filter(id__in=user_ids)
        user_dtos = []
        for user in users:
            user_dto = UserDTO(user_id=user.id,
                               name=user.name,
                               profile_pic_url=user.profile_pic_url)
            user_dtos.append(user_dto)
        return user_dtos
